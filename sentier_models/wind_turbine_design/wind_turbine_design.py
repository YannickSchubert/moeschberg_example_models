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
        pass
