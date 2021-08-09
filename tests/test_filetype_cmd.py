import pytest
from bot_commands import filetype_cmd


def test_filetype_response():

    assert type(filetype_cmd.display_file_information(".exe")) == str


    assert filetype_cmd.display_file_information(".exe") == 'An EXE file contains an executable program for Windows.  EXE is short for "executable," and it is the standard file extension used by Windows programs.  For many Windows users, EXE files are synonymous with Windows programs, making ".exe" one of the most recognizable file extensions.'
    assert filetype_cmd.display_file_information("exe") == 'An EXE file contains an executable program for Windows.  EXE is short for "executable," and it is the standard file extension used by Windows programs.  For many Windows users, EXE files are synonymous with Windows programs, making ".exe" one of the most recognizable file extensions.'

    assert filetype_cmd.display_file_information(".sln") == 'An SLN file is a structure file used for organizing projects in Microsoft Visual Studio.  It contains text-based information about the project environment and project state.'
    assert filetype_cmd.display_file_information("sln") == 'An SLN file i a structure file used for organizing projects in Microsoft Visual Studio.  It contains text-based information about the project environment and project state.'

    error_message = "```Error. Example of proper usage:\n\n%filetype .exe```"

    assert filetype_cmd.display_file_information(".fail") == error_message
    assert filetype_cmd.display_file_information("fail") == error_message
    assert filetype_cmd.display_file_information(9.5) == error_message
    assert filetype_cmd.display_file_information(111) == error_message
    assert filetype_cmd.display_file_information(-9.5) == error_message
    assert filetype_cmd.display_file_information(-111) == error_message
    assert filetype_cmd.display_file_information(["h", "e", "l", "l", "o"]) == error_message
    