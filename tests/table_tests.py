import unittest

from ddt import data, ddt, unpack

from table import Table

WIDTH_LENGTH = 4
ACTUAL_WIDTH_LENGTH = WIDTH_LENGTH - 1


@ddt
class TableTests(unittest.TestCase):
    def setUp(self):
        self.table = Table(WIDTH_LENGTH, WIDTH_LENGTH)

    @data((2, 5), (0, 0), (8, 8),)
    @unpack
    def test_table_is_created_correctly(self, width, length):
        """ Verify the table object is instantiated correctly. """
        table = Table(WIDTH_LENGTH, WIDTH_LENGTH)
        self.assertEqual(table.width, ACTUAL_WIDTH_LENGTH)
        self.assertEqual(table.length, ACTUAL_WIDTH_LENGTH)

    @data((-1, WIDTH_LENGTH), (WIDTH_LENGTH, -5),)
    @unpack
    def test_table_creation_with_negative_numbers(self, width, length):
        """ Verify an exception is raised if table is created with negative values. """
        with self.assertRaises(ValueError):
            Table(width, length)

    @data(('a', 2), (2, 'b'),)
    @unpack
    def test_string_parameters_cause_exception(self, width, length):
        """ Verify an exception is raised if table is created with string values. """
        with self.assertRaises(ValueError):
            Table(width, length)

    @data((2, True), (WIDTH_LENGTH, False), (-1, False),)
    @unpack
    def test_is_x_coordinate_on_table(self, x, expected_value):
        self.assertEqual(self.table._is_x_coordinate_on_table(x), expected_value)

    @data((2, True), (WIDTH_LENGTH, False), (-1, False),)
    @unpack
    def test_is_y_coordinate_on_table(self, y, expected_value):
        self.assertEqual(self.table._is_y_coordinate_on_table(y), expected_value)

    @data((0, 0, True), (WIDTH_LENGTH, 0, False), (-1, 0, False), (0, WIDTH_LENGTH, False), (0, -1, False),)
    @unpack
    def test_is_valid_location(self, x, y, expected_value):
        self.assertEqual(self.table.is_valid_location(x, y), expected_value)
