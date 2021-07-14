import pytest
from bot_commands import ftc_cmd


def test_ftc_response():

    assert ftc_cmd.convert_fahrenheit_to_celsius("0") == "0.0°F is -17.7778°C."
    assert ftc_cmd.convert_fahrenheit_to_celsius("-5") == "-5.0°F is -20.5556°C."
    assert ftc_cmd.convert_fahrenheit_to_celsius("-1.1") == "-1.1°F is -18.3889°C."
    assert ftc_cmd.convert_fahrenheit_to_celsius("-111.256789") == "-111.256789°F is -79.5871°C."
    assert ftc_cmd.convert_fahrenheit_to_celsius("5") == "5.0°F is -15.0°C."
    assert ftc_cmd.convert_fahrenheit_to_celsius("1.1") == "1.1°F is -17.1667°C."
    assert ftc_cmd.convert_fahrenheit_to_celsius("111.256789") == "111.256789°F is 44.0315°C."


    error_message = "```Error, please input a number. Example of proper usage:\n\n*ftc 25```"

    assert ftc_cmd.convert_fahrenheit_to_celsius(".fail") == error_message
    assert ftc_cmd.convert_fahrenheit_to_celsius("fail") == error_message
    assert ftc_cmd.convert_fahrenheit_to_celsius(["h", "e", "l", "l", "o"]) == error_message
    