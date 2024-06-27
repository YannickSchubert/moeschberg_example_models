from dataclasses import dataclass
from typing import Optional, Union


@dataclass
class Attribute:
    uri: str  # URI
    value: Optional[Union[float, str, int]]
    unit: str  # URI
