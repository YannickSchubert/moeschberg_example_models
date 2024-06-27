import windisch as windisch

from sentier_models.abstract_model.attribute import Attribute
from sentier_models.abstract_model.model import AbstractModel
from sentier_models.abstract_model.product import Product


class WindTurbineDesign(AbstractModel):

    inputs = {
        "rotor": Product(
            uri="rotor",
            value=None,
            unit="mass_unit",
            attributes=[
                Attribute(uri="location", value=None, unit="location"),
                Attribute(uri="transport_supplied", value=False, unit="boolean"),
            ],
        ),
        "nacelle": Product(
            uri="nacelle",
            value=None,
            unit="mass_unit",
            attributes=[
                Attribute(uri="location", value=None, unit="location"),
                Attribute(uri="transport_supplied", value=False, unit="boolean"),
            ],
        ),
        "tower": Product(
            uri="tower",
            value=None,
            unit="mass_unit",
            attributes=[
                Attribute(uri="location", value=None, unit="location"),
                Attribute(uri="transport_supplied", value=False, unit="boolean"),
            ],
        ),
        "electronics": Product(
            uri="electronics",
            value=None,
            unit="mass_unit",
            attributes=[
                Attribute(uri="location", value=None, unit="location"),
                Attribute(uri="transport_supplied", value=None, unit="boolean"),
            ],
        ),
        "cable": Product(
            uri="cable",
            value=None,
            unit="mass_unit",
            attributes=[
                Attribute(uri="location", value=None, unit="location"),
                Attribute(uri="transport_supplied", value=None, unit="boolean"),
            ],
        ),
        "foundation": Product(
            uri="foundation",
            value=None,
            unit="mass_unit",
            attributes=[
                Attribute(uri="location", value=None, unit="location"),
                Attribute(uri="transport_supplied", value=None, unit="boolean"),
            ],
        ),
    }

    outputs = {
        "wind_turbine": Product(
            uri="wind_turbine",
            value=None,
            unit="mass_unit",
            attributes=[
                Attribute(uri="power", value=None, unit="mass_unit"),
                Attribute(uri="location", value=None, unit="location"),
            ],
        )
    }

    def run(self):
        windisch.update_input_parameters()
        tip = windisch.TurbinesInputParameters()
        tip.sizes = [50]
        tip.application = ["offshore"]
        tip.years = [2000]
        tip.static()

        _, array = windisch.fill_xarray_from_input_parameters(tip)

        wt = windisch.WindTurbineModel(array)
        wt.set_all()
        list_mass = [
            "rotor mass",
            "nacelle mass",
            "tower mass",
            "electronics mass",
            "cable mass",
            "foundation mass",
        ]

        for mass in list_mass:
            print(mass)
            print(wt[mass].item())
