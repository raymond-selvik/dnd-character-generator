from opcode import hasname
from operator import ge
from character import Character, CharacterBuilder
from abillity import AbillityType
from skills import Skill, SkillType

def main() -> None:
    builder = CharacterBuilder()

    character = (builder
        .with_level(1)
        .with_abillity_scores(generate_scores=True)
        .build())

    print(character)
 

if __name__ == "__main__":
    main()


