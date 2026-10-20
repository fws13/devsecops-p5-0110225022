from dataclasses import dataclass, asdict


@dataclass
class Note:
    id: int
    title: str
    content: str

    def to_dict(self):
        return asdict(self)
