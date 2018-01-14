from compass import Compass
from robot import Robot
from table import Table


class CommandPanel(object):
    """ Class provides interface for commanding our robot. """
    VALID_COMMANDS = ['PLACE', 'MOVE', 'LEFT', 'RIGHT', 'REPORT']

    def __init__(self, robot):
        self.robot = robot
        self.commands_list = []

        self.commands_mapper = {
            'PLACE': (self.activate_robot, None),
            'MOVE': (self.robot.move, None),
            'LEFT': (self.robot.rotate, Compass.LEFT),
            'RIGHT': (self.robot.rotate, Compass.RIGHT),
            'REPORT': (self.print_robot_position, None),
        }

    def activate_robot(self):
        position = self.commands_list.pop(0)  # Get position and direction information in string format.
        activation_args = position.split(',')  # Get arguments for robot placement (expected [x, y, direction])
        self.robot.place(activation_args[0], activation_args[1], activation_args[2])

    def execute_commands(self, commands):
        self.commands_list = commands.split(' ')

        while self.commands_list:
            command = self.commands_list.pop(0)

            # Execute valid commands otherwise do nothing
            if command in self.VALID_COMMANDS:
                function, arg = self.commands_mapper[command]
                function(arg) if arg else function()

    def print_robot_position(self):
        print self.robot


if __name__ == '__main__':
    # User instruction messages.
    print '\n'
    print '=' * 60
    print 'Valid commands: {}'.format(CommandPanel.VALID_COMMANDS)
    print 'Command example: "PLACE 0,0,NORTH MOVE RIGHT REPORT"'
    print 'To exit press: "ctrl+c".'
    print '=' * 60
    print '\n'
    table_width = raw_input('Table width (leave empty for 5):  ') or '5'
    table_length = raw_input('Table length (leave empty for 5): ') or '5'
    table = Table(table_width, table_length)
    print 'Table created successfully. {}.'.format(table)
    command_panel = CommandPanel(Robot(table))

    while True:
        commands_string = raw_input('Enter command stream: ')
        command_panel.execute_commands(commands_string.upper())
