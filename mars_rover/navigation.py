from .rover import Rover

# INSTRUCTION_MAP keys are literal commands
# INSTRUCTION_MAP values are corresponding Rover method names
INSTRUCTION_MAP = {
    'L': 'turn_left',
    'R': 'turn_right',
    'M': 'move'
}

def navigate(rover: Rover, instructions: str):
    for instruction in instructions:
        if instruction in INSTRUCTION_MAP:
            getattr(rover, INSTRUCTION_MAP[instruction])()
