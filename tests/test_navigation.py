import pytest
from mars_rover.datastructures import Point
from mars_rover.navigation import navigate
from mars_rover.rover import Rover


# These test cases are based on README
@pytest.mark.parametrize(
    'rover, instructions, expected_point, expected_direction',
    [
        (Rover(Point(5, 5), Point(1, 2), 'N', 'Rover1'), 'LMLMLMLMM', Point(1, 3), 'N'),
        (Rover(Point(5, 5), Point(3, 3), 'E', 'Rover2'), 'MMRMMRMRRM', Point(5, 1), 'E'),
    ]
)
def test_navigation(rover, instructions, expected_point, expected_direction):
    navigate(rover, instructions)
    assert rover.current_point == expected_point
    assert rover.current_direction == expected_direction
