from typing import Dict, List

from pydantic import Field

import sentier_models.wind_turbine_design.windisch as windisch
from sentier_models.abstract_model.abstract_unit_process import AbstractUnitProcess
from sentier_models.abstract_model.attribute import Attribute
from sentier_models.abstract_model.product import Product


class WindTurbineDesign(AbstractUnitProcess):

    identifier: str = Field("wind_turbine_design", constant=True)
    preflabel: str = Field("Wind Turbine Design", constant=True)
    version: str = Field("0.1", constant=True)  # URI
    previous_version: str = Field("0.0", constant=True)  # URI
    license: str = Field("CC-BY", constant=True)  # URI
    source: str = Field("", constant=True)  # URI
    authors: List[str] = Field(["test_author"], constant=True)  # URI
    documentation: str = Field("", constant=True)  # URI
    model_instance: str = Field("", constant=True)  # URI

    inputs: Dict[str, Product] = Field(
        {
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
                attributes={
                    "location": Attribute(uri="location", value=None, unit="location"),
                    "transport_supplied": Attribute(uri="transport_supplied", value=None, unit="boolean"),
                },
            ),
        }
    )

    outputs: Dict[str, Product] = Field(
        {
            "wind_turbine": Product(
                uri="http://data.europa.eu/qw1/prodcom2023/281124",
                value=None,
                unit="mass_unit",
                attributes={
                    "power": Attribute(uri="power", value=None, unit="mass_unit"),
                    "location": Attribute(uri="location", value=None, unit="location"),
                },
            )
        }
    )

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
