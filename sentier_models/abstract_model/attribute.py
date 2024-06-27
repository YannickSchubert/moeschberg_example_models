from dataclasses import dataclass
from typing import Union


@dataclass
class Attribute:
    uri: str  # URI
    value: Union[float, str, int]
    unit: str  # URI
