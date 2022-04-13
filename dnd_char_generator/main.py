from opcode import hasname
from character import Character
from abillity import AbillityType
from skills import Skill, SkillType

def main() -> None:
    c = Character()

    print(c.abillity_scores[AbillityType.STR].modifier)

    for abillity in AbillityType:
        print(f"{abillity.name} - Value: {c.abillity_scores[abillity].score} - Modifier: {c.abillity_scores[abillity].modifier}")

    for skill in SkillType:
        print(f"{skill.name} - Modifier: {c.get_skill_modifier(skill)} - Type: {skill.value.abillity_type.value}")  

if __name__ == "__main__":
    main()


