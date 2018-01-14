class Table(object):
    """ Table representation defined by width and length dimensions. """

    def __init__(self, width, length):
        try:
            self.width = int(width) - 1
            self.length = int(length) - 1
        except ValueError:
            raise ValueError('Table dimensions must be numbers.')

        self._raise_exception_if_invalid_dimensions()

    def __str__(self):
        return 'Width: {}, Length: {}'.format(self.width + 1, self.length + 1)

    def _is_x_coordinate_on_table(self, position_x):
        """ Check that x coordinate is on the table """
        return 0 <= position_x <= self.width

    def _is_y_coordinate_on_table(self, position_y):
        """ Check that y coordinate is on the table. """
        return 0 <= position_y <= self.length

    def _raise_exception_if_invalid_dimensions(self):
        if not min(self.width, self.length) > -1:
            raise ValueError('Table dimensions can not be negative numbers.')

    def is_valid_location(self, position_x, position_y):
        return self._is_x_coordinate_on_table(position_x) and self._is_y_coordinate_on_table(position_y)
