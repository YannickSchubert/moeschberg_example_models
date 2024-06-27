from sentier_models.abstract_model.attribute import Attribute
from sentier_models.abstract_model.product import Product
from sentier_glossary import GlossaryAPI, CommonSchemes

if __name__ == "__main__":

    api = GlossaryAPI()

    print(api.schemes())

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
