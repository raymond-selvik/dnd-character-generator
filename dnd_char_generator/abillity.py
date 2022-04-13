from dataclasses import dataclass
from enum import Enum
import random
from typing import cast

class AbillityType(Enum):
    STR = "Strength"
    DEX = "Dexterity"
    CON = "Constitution"
    INT = "Intelligence"
    WIS = "Wisdom"
    CHA = "Charisma"

@dataclass
class Abillity:
    def __init__(self) -> None:
        self.score: int = self.generate_score()

    def __init(self, score: int):
        self.score = score

    @property
    def modifier(self) -> int:
        modifier_value = (self.score - 10) / 2

        return int(modifier_value)

    def generate_score(self, handicap: int = 1) -> int:
        num_of_dice = 3 + handicap

        rolls = [random.randint(1,6) for i in range(num_of_dice)]
        rolls.sort()

        for i in range(handicap):
            rolls.pop(0)

        return sum(rolls)
    



