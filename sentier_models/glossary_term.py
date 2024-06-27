from dataclasses import dataclass
from typing import Optional
from uuid import UUID


@dataclass
class Term:
    uid: str  # IRI
    name: str
    sub_class_of: str  # IRI
    data: dict

