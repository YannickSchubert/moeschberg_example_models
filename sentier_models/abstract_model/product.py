from dataclasses import dataclass
from typing import List, Optional, Union

from sentier_models.abstract_model.attribute import Attribute


@dataclass
class Product:
    uri: str  # URI
    value: Optional[Union[float, str, int]]
    unit: str  # URI
    attributes: List[Attribute]  # List of Attribute objects
