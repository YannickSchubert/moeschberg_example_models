from typing import List, Dict

import windisch as windisch

from sentier_models.abstract_model.attribute import Attribute
from sentier_models.abstract_model.model import AbstractModel
from sentier_models.abstract_model.product import Product


class WindTurbineDesign(AbstractModel):

    identifier: str = "wind_turbine_design"
    preflabel: str = "Wind Turbine Design"
    version: str = "0.1"  # URI
    previous_version: str = "0.0"  # URI
    license: str = "CC-BY"  # URI
    source: str = ""  # URI
    authors: List[str] = []  # URI
    documentation: str = ""  # URI
    model_instance: str = ""  # URI

    inputs: Dict[str, Product] = {
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

    outputs: Dict[str, Product] = {
        "wind_turbine": Product(
            uri="http://data.europa.eu/qw1/prodcom2023/281124",
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
        input_items = self.inputs.keys()

        for input in input_items:
            self.inputs[input].value = wt[f"{input} mass"].item()
            print(wt[[f"{input} mass"]].item())
