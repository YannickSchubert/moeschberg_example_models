from sentier_glossary import GlossaryAPI

from sentier_models.abstract_model.attribute import Attribute
from sentier_models.abstract_model.product import Product
from sentier_models.wind_turbine_design.wind_turbine_design import WindTurbineDesign

if __name__ == "__main__":

    search_for = "Wind turbines"

    api = GlossaryAPI()
    concepts = [
        concept
        for concept in api.concepts_for_scheme("http://data.europa.eu/qw1/prodcom2023/prodcom2023")
        if "wind turbines" in concept["prefLabel"].lower()
    ]
    wind_turbine_iri = concepts[0]["iri"]

    wind_turbine = Product(
        uri=wind_turbine_iri,
        value=1,
        unit="piece_unit",
        attributes={
            "location": Attribute(uri="location", value="denmark", unit="location"),
            "application": Attribute(uri="offshore", value="offshore", unit="categorial"),
            "power": Attribute(uri="power", value=200, unit="power_unit"),
        },
    )
    print(wind_turbine)

    # TODO: orchestrator should find the model based on the product

    model = WindTurbineDesign()
    model.outputs["wind_turbine"] = wind_turbine
    model.run()

    print(model.inputs)
