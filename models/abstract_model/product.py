from typing import List, Union

from models.abstract_model.attribute import Attribute


class Product:
    uri: str  # URI
    value: Union[float, str, int]
    unit: str  # URI
    attributes: List[Attribute]  # List of Attribute objects
