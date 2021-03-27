from .datastructures import Point


class Rover():
    DIRECTIONS = ('N', 'E', 'S', 'W')

    def __init__(self, max_point: Point, landing_point: Point, direction: str, name: str):
        assert direction in self.DIRECTIONS, \
            f'Invalid direction {direction}; expected one of {self.DIRECTIONS}'
        assert max_point.x > 0 and max_point and max_point.y > 0, \
            f'Invalid max point {max_point}'

        self.min_point = Point(0, 0)
        self.max_point = max_point
        self.current_point = landing_point
        self.current_direction = direction
        self.name = name

    def can_move(self) -> bool:
        ''' Returns True if Rover can move in the current direction and False otherwise. '''
        if self.current_direction == 'N':
            return self.current_point.y < self.max_point.y
        if self.current_direction == 'E':
            return self.current_point.x < self.max_point.x
        if self.current_direction == 'S':
            return self.current_point.y > self.min_point.y
        if self.current_direction == 'W':
            return self.current_point.x > self.min_point.x
        return False

    def turn_right(self) -> None:
        ''' Turns rover right: N -> E -> S -> W -> N. Changes rover's current_direction. '''
        i = (self.DIRECTIONS.index(self.current_direction) + 1) % len(self.DIRECTIONS)
        self.current_direction = self.DIRECTIONS[i]

    def turn_left(self) -> None:
        ''' Turns rover left: N <- E <- S <- W <- N. Changes rover's current_direction. '''
        i = self.DIRECTIONS.index(self.current_direction) - 1
        self.current_direction = self.DIRECTIONS[i]

    def move(self) -> None:
        if self.can_move():
            if self.current_direction == 'N':
                self.current_point.y += 1
            elif self.current_direction == 'E':
                self.current_point.x += 1
            elif self.current_direction == 'S':
                self.current_point.y -= 1
            elif self.current_direction == 'W':
                self.current_point.x -= 1
        else:
            pass # TODO
