import pytest
from mars_rover.datastructures import Point
from mars_rover.rover import Rover


@pytest.mark.parametrize(
    'landing_point, direction, expected',
    [
        (Point(9, 8), 'N', False),
        (Point(9, 7), 'N', True),
        (Point(9, 7), 'E', False),
        (Point(8, 7), 'E', True),
        (Point(8, 0), 'S', False),
        (Point(8, 1), 'S', True),
        (Point(0, 1), 'W', False),
        (Point(1, 1), 'W', True),
    ]
)
def test_rover_can_move(landing_point, direction, expected):
    rover = Rover(
        max_point = Point(9, 8),
        landing_point = landing_point,
        direction = direction,
        name = 'Perseverance'
    )
    assert rover.can_move() == expected


@pytest.mark.parametrize(
    'old_direction, new_direction',
    [
        ('N', 'E'),
        ('E', 'S'),
        ('S', 'W'),
        ('W', 'N'),
    ]
)
def test_rover_turn_right(old_direction, new_direction):
    rover = Rover(Point(5, 5), Point(0, 0), old_direction, 'Perseverance')
    rover.turn_right()
    assert rover.current_direction == new_direction


@pytest.mark.parametrize(
    'old_direction, new_direction',
    [
        ('N', 'W'),
        ('W', 'S'),
        ('S', 'E'),
        ('E', 'N'),
    ]
)
def test_rover_turn_left(old_direction, new_direction):
    rover = Rover(Point(5, 5), Point(0, 0), old_direction, 'Perseverance')
    rover.turn_left()
    assert rover.current_direction == new_direction


@pytest.mark.parametrize(
    'old_point, direction, new_point',
    [
        (Point(2, 2), 'N', Point(2, 3)),
        (Point(2, 2), 'E', Point(3, 2)),
        (Point(2, 2), 'S', Point(2, 1)),
        (Point(2, 2), 'W', Point(1, 2)),
    ]
)
def test_valid_move(old_point, direction, new_point):
    rover = Rover(Point(5, 5), old_point, direction, 'Perseverance')
