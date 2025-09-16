from dataclasses import dataclass, field

@dataclass
class Pokemon:
    name: str
    url: str
    abilities: list = field(default_factory=list)
    moves: list = field(default_factory=list)
    stats: list = field(default_factory=list)

    def validate_structure(self) -> bool:
        if not isinstance(self.name, str) or not self.name:
            return False
        if not isinstance(self.url, str) or not self.url.startswith("https://"):
            return False
        if not all(isinstance(x, list) for x in [self.abilities, self.moves, self.stats]):
            return False
        return True
