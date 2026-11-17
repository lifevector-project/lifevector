from dataclasses import dataclass


@dataclass
class Role:
    name: str
    sort_order: int
    description: str | None = None
    is_active: bool = True    
    id: int | None = None
