from collections import namedtuple
from dataclasses import dataclass
from enum import Enum
from re import M
from typing import NamedTuple, Tuple

from dnd_char_generator.abillity import AbillityType

@dataclass
class Skill:
    name: str
    abillity_type: AbillityType

class SkillType(Enum):
    Atletics: Skill = Skill("Atletics", AbillityType.STR)
    Acrobatics: Skill = Skill("Acrobatics", AbillityType.DEX)
    Arcana: Skill = Skill("Arcana", AbillityType.INT)
    Survial: Skill = Skill("Survial", AbillityType.WIS)
    Deception: Skill = Skill("Deception", AbillityType.CHA)
