import pytest
from bot_commands import ctf_cmd


def test_ctf_response():

    assert ctf_cmd.convert_celsius_to_fahrenheit("0") == "0.0°C is 32.0°F."
    assert ctf_cmd.convert_celsius_to_fahrenheit("-5") == "-5.0°C is 23.0°F."
    assert ctf_cmd.convert_celsius_to_fahrenheit("-1.1") == "-1.1°C is 30.02°F."
    assert ctf_cmd.convert_celsius_to_fahrenheit("-111.256789") == "-111.256789°C is -168.2622°F."
    assert ctf_cmd.convert_celsius_to_fahrenheit("5") == "5.0°C is 41.0°F."
    assert ctf_cmd.convert_celsius_to_fahrenheit("1.1") == "1.1°C is 33.98°F."
    assert ctf_cmd.convert_celsius_to_fahrenheit("111.256789") == "111.256789°C is 232.2622°F."


    error_message = "```Error, please input a number. Example of proper usage:\n\n*ctf 20```"

    assert ctf_cmd.convert_celsius_to_fahrenheit(".fail") == error_message
    assert ctf_cmd.convert_celsius_to_fahrenheit("fail") == error_message
    assert ctf_cmd.convert_celsius_to_fahrenheit(["h", "e", "l", "l", "o"]) == error_message
