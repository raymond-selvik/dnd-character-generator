from operator import mod
from typing import List
from abillity import Abillity, AbillityType
from skills import Skill, SkillType


class Character:
    prof_skills: List[SkillType] = [SkillType.Atletics, SkillType.Acrobatics]
    saving_throws = List[AbillityType] = [AbillityType.DEX]

    def __init__(self, level: int = 1) -> None:
        self.level = level
        self.abillity_scores = self.generate_abillity_scores()

    @property
    def prof_bonus(self) -> int:
        return int((self.level - 1) / 4) + 2
    
    def generate_abillity_scores(self) -> dict[AbillityType, Abillity]:
        scores = {}
        for type in AbillityType:
            scores[type] = Abillity()
        
        return scores

    def get_skill_modifier(self,skill: SkillType) -> int:
        modifier = self.abillity_scores[skill.value.abillity_type].modifier

        if skill in self.prof_skills:
            modifier += self.prof_bonus
        
        return modifier

    def get_saving_throw_modifier(self, abillity: AbillityType) -> int:
        modifier = self.abillity_scores[abillity].modifier

        if abillity in self.saving_throws:
            modifier += self.prof_bonus
        
        return modifier



