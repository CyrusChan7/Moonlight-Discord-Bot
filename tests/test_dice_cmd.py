import pytest
from bot_commands import dice_cmd


def test_number_generation():
    """ Tests whether dice_cmd.py generates the correct number - between 1 (inclusive) and 6 (inclusive) """

    assert type(dice_cmd.roll_dice()) == int

    for i in range(1000):       # Test 1000 times because the rolling num result will differ every time,
                                # we want to be absolutely certain that it is generating the correct numbers
        rolled_num = dice_cmd.roll_dice()
        assert rolled_num >= 1 and rolled_num <= 6
