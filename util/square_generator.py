class Square:
    def __init__(self, x, y, id=None):
        self.id = id
        self.description = None
        self.game_exit = False
        self.x = x
        self.y = y
        self.up_to = None
        self.down_to = None
        self.right_to = None
        self.left_to = None
        self.sides = {'up': True, 'down': True, 'left': True, 'right': True}
        self.outstanding = True
        self.contents = []
        self.players = []

    def __str__(self):
        section = '-' * 30
        room = f'\nYou are in room number: {self.id}'
        coordinates = f'\n(your coordinates are: {self.x}, {self.y})'
        options = f'\n\nOptions: \n  above you is: {self.up_to}\n  below you is: {self.down_to}\n  left is: {self.left_to}\n  right is: {self.right_to}'
        contents = f'\n\nThis room contains: \n  {self.contents}'
        players = f'\n\nOther players in the room: \n  {self.players}'

        return f'\n{section}\n{room}{coordinates}{options}{contents}{players}\n\n{section}'

    side_pairs = {'up': 'down', 'down': 'up', 'left': 'right', 'right': 'left'}

    def connect_squares(self, adjacent_square, side):
        # remove adjoining side to create route
        self.sides[side] = False
        adjacent_square.sides[Square.side_pairs[side]] = False

    def set_connecting_square(self, adjacent_square, direction):
        # set apposing direction for adjacent square
        opposite_direction = Square.side_pairs[direction]
        # add adjacent square name to the direction
        setattr(self, f"{direction}_to", adjacent_square.id)
        setattr(adjacent_square, f"{opposite_direction}_to", self.id)