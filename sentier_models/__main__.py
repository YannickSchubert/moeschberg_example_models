from sentier_models.abstract_model.attribute import Attribute
from sentier_models.abstract_model.product import Product
from sentier_glossary import GlossaryAPI, CommonSchemes

from sentier_models.wind_turbine_design.wind_turbine_design import WindTurbineDesign

if __name__ == "__main__":

    api = GlossaryAPI()

    # TODO: find winc turbine in glossary...
    #print(api.schemes())
    #print(api.semantic_search("piggies", CommonSchemes.cn2024))

    wind_turbine = Product(
        uri="wind_turbine",
        value=1,
        unit="mass_unit",
        attributes=[
            Attribute(uri="power", value=1, unit="mass_unit"),
            Attribute(uri="location", value="denmark", unit="location"),
        ],
    )
    print(wind_turbine)

    # TODO: orchestrator should find the model based on the product

    model = WindTurbineDesign()
    model.inputs = [wind_turbine]
    model.run()

    print(model.outputs)
