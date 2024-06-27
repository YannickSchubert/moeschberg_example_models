from typing import List, Dict

from sentier_models.abstract_model.product import Product
from dataclasses import dataclass, field


@dataclass
class AbstractModel:
    identifier: str = ""
    preflabel: str = ""
    version: str = ""  # URI
    previous_version: str = ""  # URI
    license: str = ""  # URI
    source: str = ""  # URI
    authors: List[str] = field(default_factory=lambda: [])  # URI
    documentation: str = ""  # URI
    model_instance: str = ""  # URI

    inputs: Dict[str, Product] = field(default_factory=lambda: {})
    outputs: Dict[str, Product] = field(default_factory=lambda: {})

    def run(self):
        pass
