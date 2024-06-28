from dataclasses import dataclass


@dataclass
class Term:
    uid: str  # IRI
    name: str
    sub_class_of: str  # IRI
    data: dict
