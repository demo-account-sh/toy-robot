from compass import Compass
from table import Table


class Robot(object):
    """
        Base robot class which can move in different dirrections
        depending on the current state and the command given.
        Robot can move once placed on a table. Movement is restricted
        by table size.
    """
    def __init__(self, table):
        if not isinstance(table, Table):
            raise ValueError('This robot needs a Table class instance.')

        self.is_active = False
        self.direction = None
        self.position = {'x': None, 'y': None}
        self.table = table

    def __str__(self):
        return '{},{},{}'.format(self.position['x'], self.position['y'], self.direction)

    def _set_new_direction(self, direction, rotation_angle=None):
        self.direction = Compass.get_new_direction(direction, rotation_angle)
        print 'Direction: {}.'.format(self.direction)

    def _set_new_position(self, position_x, position_y):
        if self.table.is_valid_location(position_x, position_y):
            self.position = {'x': position_x, 'y': position_y}
            print 'Position: {},{}.'.format(self.position['x'], self.position['y'])

    def place(self, position_x, position_y, direction):
        """
            Places robot on table depending on x and y
            coordinates facing towards direction.
        """
        try:
            position_x = int(position_x)
            position_y = int(position_y)
        except (ValueError, TypeError):
            raise ValueError('Both coordinate values need to be numbers.')

        # Check if the coordinates are on the table otherwise do nothing
        if self.table.is_valid_location(position_x, position_y):
            self.is_active = True
            self._set_new_direction(direction)
            self._set_new_position(position_x, position_y)
            print 'Robot placed!'

    def move(self):
        """ Moves robot one 'field' towards the facing direction. """
        if self.is_active:
            new_x, new_y = Compass.get_new_position(
                self.position['x'],
                self.position['y'],
                self.direction
            )
            self._set_new_position(new_x, new_y)

    def rotate(self, angle):
        """ Changes facing depending on the angle and current facing. """
        if self.is_active:
            self._set_new_direction(self.direction, angle)
