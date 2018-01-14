class Compass(object):
    """
        Class that contains and calculates information about
        orijentation, movement vectors and rotation direction.
    """
    # Constants for facing
    NORTH = 'NORTH'
    EAST = 'EAST'
    SOUTH = 'SOUTH'
    WEST = 'WEST'
    VALID_DIRECTIONS = [NORTH, EAST, SOUTH, WEST]

    # Constants for rotation
    LEFT = -90
    RIGHT = 90
    VALID_ROTATION_ANGLES = [LEFT, RIGHT]

    # Dict for mapping facing with movement direction values
    DIRECTION_MAPPER = {
        NORTH: (0, 1),
        EAST: (1, 0),
        WEST: (-1, 0),
        SOUTH: (-1, -1),
    }

    # Dict for mapping current facing and facing after rotation
    DIRECTION_ROTATION_MAPPER = {
        NORTH: {LEFT: WEST, RIGHT: EAST},
        EAST: {LEFT: NORTH, RIGHT: SOUTH},
        SOUTH: {LEFT: EAST, RIGHT: WEST},
        WEST: {LEFT: SOUTH, RIGHT: NORTH},
    }

    @classmethod
    def calculate_position_x(cls, position_x, direction):
        """ Returns new x axis position based on current facing and x axis. """
        cls.raise_exception_if_invalid_direction(direction)
        return position_x + cls.DIRECTION_MAPPER[direction][0]

    @classmethod
    def calculate_position_y(cls, position_y, direction):
        """ Returns new y axis position based on current facing and y axis. """
        cls.raise_exception_if_invalid_direction(direction)
        return position_y + cls.DIRECTION_MAPPER[direction][1]

    @classmethod
    def get_new_direction(cls, old_direction, rotation_angle=None):
        """ Returns new facing based on current direction and rotation angle. """
        if not rotation_angle:
            return old_direction

        cls.raise_exception_if_invalid_direction(old_direction)
        cls.raise_exception_if_invalid_rotation(rotation_angle)
        return cls.DIRECTION_ROTATION_MAPPER[old_direction][rotation_angle]

    @classmethod
    def get_new_position(cls, position_x, position_y, direction):
        """ Returns new x and y coordinates base on old location and facing. """
        new_position_x = cls.calculate_position_x(position_x, direction)
        new_position_y = cls.calculate_position_y(position_y, direction)
        return new_position_x, new_position_y

    @classmethod
    def is_valid_direction(cls, direction):
        return direction in cls.VALID_DIRECTIONS

    @classmethod
    def is_valid_rotation(cls, rotation_angle):
        return rotation_angle in cls.VALID_ROTATION_ANGLES

    @classmethod
    def raise_exception_if_invalid_direction(cls, direction):
        if not cls.is_valid_direction(direction):
            raise ValueError('Invalid direction: "{}"'.format(direction))

    @classmethod
    def raise_exception_if_invalid_rotation(cls, angle):
        if not cls.is_valid_rotation(angle):
            raise ValueError('Invalid rotation angle: "{}"'.format(angle))
