import argparse
from typing import Dict

from sentier_glossary import GlossaryAPI

from sentier_models import all_models
from sentier_models.abstract_model.attribute import Attribute
from sentier_models.abstract_model.product import Product


models_by_output_iri: Dict[str, list] = {}
for model in all_models:
    for output_name, output_schema in model.model_fields['outputs'].default.items():
        uri = output_schema.uri
        if uri not in models_by_output_iri:
            models_by_output_iri[uri] = []
        models_by_output_iri[uri].append(model)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("search_product", type=str, nargs='?', default="Wind turbines", help="Search for a product")
    search_for = parser.parse_args().search_product

    api = GlossaryAPI()
    concepts = [
        concept
        for concept in api.concepts_for_scheme("http://data.europa.eu/qw1/prodcom2023/prodcom2023")
        if "wind turbines" in concept["prefLabel"].lower()
    ]
    product_iri = concepts[0]["iri"]

    product = Product(
        uri=product_iri,
        value=1,
        unit="piece_unit",
        attributes={
            "location": Attribute(uri="location", value="denmark", unit="location"),
            "application": Attribute(uri="offshore", value="offshore", unit="categorial"),
            "power": Attribute(uri="power", value=200, unit="power_unit"),
        },
    )

    # find model:
    possible_models = models_by_output_iri[product_iri]

    # TODO let user choose between found models...
    selected_model_class = possible_models[0]

    # find model output name to use
    for output_name, output_schema in selected_model_class.model_fields['outputs'].default.items():
        if output_schema.uri == product_iri:
            model_output_name = output_name
            break

    model_instance = selected_model_class()
    model_instance.outputs[model_output_name] = product
    model_instance.run()

    print(model_instance.inputs)
