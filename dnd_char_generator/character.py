import math
from operator import mod
from typing import Dict, List
from dnd_char_generator.abillity import Abillity, AbillityType
from dnd_char_generator.skills import SkillType


class Character:
    def __init__(self, level: int = 1) -> None:
        self.level: int = level
        self.abillity_scores: Dict(AbillityType, Abillity) = dict()
        self.prof_skills: List[SkillType] = list()
        self.saving_throws: List(AbillityType) = list()

    @property
    def prof_bonus(self) -> int:
        return math.floor((self.level - 1) / 4) + 2

    def set_level(self, lvl: int) -> None:
        self.level = lvl
    
    def set_skills(self, skills: List[SkillType]) -> None:
        self.prof_skills.extend(skills)

    def get_skill_modifier(self,skill: SkillType) -> int:
        modifier = self.abillity_scores[skill.value.abillity_type].modifier

        if skill in self.prof_skills:
            modifier += self.prof_bonus
        
        return modifier

    def set_saving_throws(self, saving_throw: List[AbillityType]) -> None:
        self.saving_throws.extend(saving_throw)

    def get_saving_throw_modifier(self, abillity: AbillityType) -> int:
        modifier = self.abillity_scores[abillity].modifier

        if abillity in self.saving_throws:
            modifier += self.prof_bonus
        
        return modifier

    def __repr__(self) -> str:
        return f"""
            Character Level: {self.level}
            Abillity Scores: {self.abillity_scores}
        """

class CharacterBuilder:
    
    def __init__(self) -> None:
        self._character = Character()

    def with_level(self, lvl: int) -> "CharacterBuilder":
        self._character.set_level(lvl)
        return self

    def with_abillity_scores(self, generate_scores: bool, scores: Dict[AbillityType, Abillity] = None) -> "CharacterBuilder":
        if generate_scores and scores is None:
            scores = {}
            for type in AbillityType:
                scores[type] = Abillity()

        self._character.abillity_scores = scores
        
        return self
    
    def with_prof_skills(self, skills: List[SkillType]) -> "CharacterBuilder":
        self._character.set_skills(skills)
        return self
    
    def with_saving_throws(self, saving_throws: List[AbillityType]) -> "CharacterBuilder":
        self._character.set_saving_throws(saving_throws)
        return self

    def build(self) -> Character:
        return self._character





