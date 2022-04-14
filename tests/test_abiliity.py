from urllib.request import AbstractBasicAuthHandler
from dnd_char_generator.abillity import Abillity
from tests.utils.ability_utils import AbillityUtils


def test_abillity_modifier_calculation():
    for value, modifier in AbillityUtils.modifier_by_abillity.items():
        abillity = Abillity(value)

        assert abillity.modifier == modifier

