import logging
import re
from io import TextIOBase

from .datastructures import Point
from .navigation import navigate
from .rover import Rover


# Exit codes
SUCCESS = 0
ERR_NO_PLATEAU_DEFINITION = 1
ERR_NO_LANDING_INSTRUCTIONS = 2
ERR_INVALID_INSTRUCTION = 3


logger = logging.getLogger(__name__)


plateau_matcher = re.compile(r'Plateau:(\d+)\s+(\d+)')
landing_matcher = re.compile(r'(\S+)\s+Landing:(\d+)\s+(\d+)\s(' + '|'.join(Rover.DIRECTIONS) + ')')
instruction_matcher = re.compile(r'(\S+)\s+Instructions:([LRM]+)')
blank_line = re.compile(r'^\s+$')


def main(input_stream: TextIOBase, output_stream: TextIOBase) -> int:
    max_point = None
    rovers = {}

    for i, line in enumerate(input_stream):
        line_no = i + 1

        # Ignore blank lines
        if blank_line.match(line):
            continue

        # Attempt to parse plateau information
        match = plateau_matcher.match(line)
        if match:
            x, y = match.groups()
            max_point = Point(int(x), int(y))
            continue

        # Attempt to parse landing information
        match = landing_matcher.match(line)
        if match:
            if not max_point:
                logger.error(f'Received landing instructions without plateau definition on line {line_no}')
                return ERR_NO_PLATEAU_DEFINITION
            rover_name, x, y, direction  = match.groups()
            rovers[rover_name] = Rover(
                max_point,
                Point(int(x), int(y)),
                direction,
                rover_name
            )
            continue

        # Attempt to parse moving instructions
        match = instruction_matcher.match(line)
        if match:
            rover_name, instructions = match.groups()
            rover = rovers.get(rover_name)
            if rover:
                # Execute rover instructions
                navigate(rovers[rover_name], instructions)
                output_stream.write(f'{rover_name}:{rover.current_point.x} {rover.current_point.y} {rover.current_direction}\n')
                continue
            else:
                logger.error(f'Received instructions for rover without landing on line {line_no}')
                return ERR_NO_LANDING_INSTRUCTIONS

        # If we are here we got some sort of invalid instruction
        logger.error(f'Unrecognized instruction in line {line_no}')
        return ERR_INVALID_INSTRUCTION

    return SUCCESS
