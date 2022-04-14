from dnd_char_generator.character import Character
from tests.utils.character_utils import CharacterUtils


def test_prof_bonus_by_level():
    for level, bonus in CharacterUtils.prof_bonus_by_level.items():
        character = Character(level)

        assert character.prof_bonus == bonus