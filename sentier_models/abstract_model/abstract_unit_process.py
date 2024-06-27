from typing import Dict, List

from pydantic import BaseModel, Field

from sentier_models.abstract_model.product import Product


class AbstractUnitProcess(BaseModel):
    identifier: str = Field("", constant=True)
    preflabel: str = Field("", constant=True)
    version: str = Field("", constant=True)  # URI
    previous_version: str = Field("", constant=True)  # URI
    license: str = Field("", constant=True)  # URI
    source: str = Field("", constant=True)  # URI
    authors: List[str] = Field([], constant=True)  # URI
    documentation: str = Field("", constant=True)  # URI
    instance: str = Field("", constant=True)  # URI

    inputs: Dict[str, Product] = Field(default={})
    outputs: Dict[str, Product] = Field(default={})

    def run(self):
        pass
