from typing import List

from models.abstract_model.product import Product


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
