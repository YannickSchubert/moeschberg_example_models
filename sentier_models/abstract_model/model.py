from typing import List

from sentier_models.abstract_model.product import Product
from dataclasses import dataclass


@dataclass
class AbstractModel:
    identifier: str
    preflabel: str
    version: str  # URI
    previous_version: str  # URI
    license: str  # URI
    source: str  # URI
    authors: List[str]  # URI
    documentation: str  # URI
    model_instance: str  # URI

    inputs: List[Product]
    outputs: List[Product]

    def run():
        pass
