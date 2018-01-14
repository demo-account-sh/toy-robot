import unittest

from ddt import data, ddt, unpack

from compass import Compass
from robot import Robot
from table import Table

MAX_VALUE = 5  # User entered value
ACTUAL_MAX_VALUE = MAX_VALUE - 1  # This will be the maximum value for x and y
MIN_VALUE = 0  # Lower limit for x and y coordinates
DEFAULT_DIRECTION = Compass.NORTH


@ddt
class RobotTests(unittest.TestCase):

    def setUp(self):
        self.table = Table(MAX_VALUE, MAX_VALUE)
        self.robot = Robot(self.table)
        self.robot.place(MIN_VALUE, MIN_VALUE, DEFAULT_DIRECTION)

    @staticmethod
    def get_position_dict(x, y):
        return {'x': x, 'y': y}

    def test_robot_creation(self):
        """ Verify robot is created as expected. """
        robot = Robot(self.table)
        self.assertEqual(robot.is_active, False)
        self.assertEqual(robot.direction, None)
        self.assertEqual(robot.position, self.get_position_dict(None, None))
        self.assertEqual(robot.table, self.table)

    def test_place(self):
        """ Verify place method works as expected. """
        self.robot.place(MIN_VALUE, MIN_VALUE, DEFAULT_DIRECTION)
        self.assertEqual(self.robot.position, self.get_position_dict(MIN_VALUE, MIN_VALUE))
        self.assertEqual(self.robot.direction, DEFAULT_DIRECTION)

    @data(('s', MIN_VALUE),  (MIN_VALUE, 's'),)
    @unpack
    def test_place_raises_exception(self, x, y):
        """ Verify place will rase exception when string is send for coordinate. """
        with self.assertRaises(ValueError):
            self.robot.place(x, y, DEFAULT_DIRECTION)

    @data(
        (MIN_VALUE - 1, MIN_VALUE),
        (MIN_VALUE, MIN_VALUE - 1),
        (ACTUAL_MAX_VALUE, ACTUAL_MAX_VALUE + 1),
        (ACTUAL_MAX_VALUE + 1, ACTUAL_MAX_VALUE),
    )
    @unpack
    def test_place_with_invalid_coordinates(self, x, y):
        """ Verify place will not move the robot with coordinates out of range. """
        expected_position = self.robot.position
        self.robot.place(x, y, DEFAULT_DIRECTION)
        self.assertEqual(self.robot.position, expected_position)

    @data(
        (1, 0, 1),
        (2, 0, 2),
        (3, 0, 3),
        (4, 0, 4),
        (5, 0, 4),
    )
    @unpack
    def test_move(self, number_of_moves, expected_x, expected_y):
        """ Verify robot position after moving. """
        for _ in xrange(number_of_moves):
            self.robot.move()
        self.assertEqual(self.robot.position, self.get_position_dict(expected_x, expected_y))

    @data(
        (1, Compass.RIGHT, Compass.EAST),
        (2, Compass.RIGHT, Compass.SOUTH),
        (3, Compass.RIGHT, Compass.WEST),
        (4, Compass.RIGHT, Compass.NORTH),
        (1, Compass.LEFT, Compass.WEST),
        (2, Compass.LEFT, Compass.SOUTH),
        (3, Compass.LEFT, Compass.EAST),
        (4, Compass.LEFT, Compass.NORTH),
    )
    @unpack
    def test_rotate(self, number_of_rotations, angle, direction):
        """ Verify rotate method faces robot in expected direction. """
        for _ in xrange(number_of_rotations):
            self.robot.rotate(angle)
        self.assertEqual(self.robot.direction, direction)

    @data((MIN_VALUE, MIN_VALUE), (ACTUAL_MAX_VALUE, ACTUAL_MAX_VALUE))
    @unpack
    def test_set_new_position(self, x, y):
        """ Verify method will set robot position as expected. """
        self.robot._set_new_position(x, y)
        self.assertEqual(self.robot.position, self.get_position_dict(x, y))

    @data(
        (MIN_VALUE - 1, MIN_VALUE),
        (MIN_VALUE, MIN_VALUE - 1),
        (ACTUAL_MAX_VALUE + 1, ACTUAL_MAX_VALUE),
        (ACTUAL_MAX_VALUE, ACTUAL_MAX_VALUE + 1),
    )
    @unpack
    def test_set_new_position_for_invalid_coordinates(self, x, y):
        """ Verify method will not change position if new coordinates are out of bounds. """
        self.robot._set_new_position(x, y)
        self.assertNotEqual(self.robot.position, self.get_position_dict(x, y))

    @data(
        (Compass.NORTH, Compass.RIGHT, Compass.EAST),
        (Compass.EAST, Compass.RIGHT, Compass.SOUTH),
        (Compass.NORTH, Compass.LEFT, Compass.WEST),
        (Compass.WEST, Compass.LEFT, Compass.SOUTH),
    )
    @unpack
    def test_set_new_direction(self, direction, angle, expected_direction):
        """ Verify method will set robot facing as expected. """
        self.robot._set_new_direction(direction, angle)
        self.assertEqual(self.robot.direction, expected_direction)

    def test_set_new_direction_when_inactive(self):
        """ Verify method will not change direction when robon inactive. """
        new_direction = Compass.EAST
        robot = Robot(self.table)
        robot._set_new_direction(new_direction, Compass.RIGHT)
        self.assertNotEqual(robot.direction, new_direction)
