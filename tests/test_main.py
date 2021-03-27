from io import StringIO

import pytest
from mars_rover.main import (ERR_INVALID_INSTRUCTION,
                             ERR_NO_LANDING_INSTRUCTIONS,
                             ERR_NO_PLATEAU_DEFINITION, SUCCESS, main)

VALID_INPUT = '''
Plateau:5 5
Rover1 Landing:1 2 N
Rover1 Instructions:LMLMLMLMM
Rover2 Landing:3 3 E
Rover2 Instructions:MMRMMRMRRM
'''


EXPECTED_OUTPUT = '''Rover1:1 3 N
Rover2:5 1 E
'''


def test_main_with_valid_input():
    in_stream = StringIO(VALID_INPUT)
    in_stream.seek(0)
    out_stream = StringIO()

    result = main(in_stream, out_stream)
    out_stream.seek(0)

    assert result == SUCCESS
    assert out_stream.read() == EXPECTED_OUTPUT


@pytest.mark.parametrize(
    'input_value, expected_error',
    [
        ('Nonesuch', ERR_INVALID_INSTRUCTION),
        ('Plateau:5 5\nRover1 Instructions:M\n', ERR_NO_LANDING_INSTRUCTIONS),
        ('Rover1 Landing:1 2 N\nRover1 Instructions:M', ERR_NO_PLATEAU_DEFINITION),
    ]
)
def test_main_with_invalid_input(input_value, expected_error):
    in_stream = StringIO(input_value)
    in_stream.seek(0)
    out_stream = StringIO()

    result = main(in_stream, out_stream)
    out_stream.seek(0)

    assert result == expected_error
    assert out_stream.read() == ''
