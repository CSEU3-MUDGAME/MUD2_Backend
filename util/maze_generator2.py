import random

class Square:
    def __init__(self, x, y):
        self.id = None
        self.description = None
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
        
        sides = ''
        for key in self.sides:
            # if key == False:
                print(key)

        def listToString(list):
            output = ''
            for value in list:
                output += value
            return output

        room = f'\nYou are in room number: {self.id}'
        coordinates = f'\n(your coordinates are: {self.x}, {self.y})'
        options = f'\n\nYou can move: \n'

        return listToString(sides)

        # return f"{room}{coordinates}{options}"

    side_pairs = {'up': 'down', 'down': 'up', 'left': 'right', 'right': 'left'}

    def connect_squares(self, adjacent_square, side):
        # remove adjoining side to create route
        self.sides[side] = False
        adjacent_square.sides[Square.side_pairs[side]] = False

    def set_connecting_square(self, adjacent_square, direction):
        # set apposing direction for adjacent square
        apposing_side = Square.side_pairs[direction]
        # add adjacent square name to the direction
        setattr(self, f"{direction}_to", adjacent_square.id)
        setattr(adjacent_square, f"{apposing_side}_to", self.id)

class Maze:
    
    def __init__(self, height, width):

        self.height = height
        self.width = width
        self.num_rooms = height * width

        # -------------------------------------------------------
        self.maze_map = [[Square(x, y) for y in range(width)] for x in range(height)]

        i = 0
        for array in self.maze_map:
            for square in array:
                square.id = i
                i += 1
        # -------------------------------------------------------

    def square_at(self, x, y):
        # Return Square at (x,y)
        return self.maze_map[x][y]

    def __str__(self):
        # Return a (crude) string representation of the maze

        maze_rows = ['-' * self.height*2]
        for y in range(self.width):
            maze_row = ['|']
            for x in range(self.height):
                if self.maze_map[x][y].sides['right']:
                    maze_row.append(' |')
                else:
                    maze_row.append('  ')
            maze_rows.append(''.join(maze_row))
            maze_row = ['|']
            for x in range(self.height):
                if self.maze_map[x][y].sides['down']:
                    maze_row.append('-+')
                else:
                    maze_row.append(' +')
            maze_rows.append(''.join(maze_row))
        
        dimensions = f"\n\nWorld\n  height: {self.height}\n  height: {self.width},\n"

        return '\n'.join(maze_rows)

    def get_adjacent_squares(self, current):
        # set the direction as coordinate movements
        directions = [('left', (-1, 0)),
                      ('right', (1, 0)),
                      ('down', (0, 1)),
                      ('up', (0, -1))]
        # initialise an emtpy list of adjacent squares
        adjacent_squares = []

        # for each direction retrieve the adjacent square
        for direction, (direction_x, direction_y) in directions:
            # set the coordinates of the adjacent square
            new_x = current.x + direction_x
            new_y = current.y + direction_y
            # check the coordinates are within the defined grid
            if (0 <= new_x < self.height) and (0 <= new_y < self.width):
                # get the adjacent square using new coordinates
                adjacent_square = maze.square_at(new_x, new_y)
                # if this adjacent square has not been visited (has) all sides
                if adjacent_square.outstanding:
                    # then add this square to the list of adjacents
                    adjacent_squares.append((direction, adjacent_square))
        # return the list of adjacent squares
        return adjacent_squares

    def create_maze(self):
        # set current position to coordinates 0,0
        current_x = 0
        current_y = 0
        # Get the square at the initial coordinates
        current_square = self.square_at(current_x, current_y)

        # create an empty stack of squares to be 
        square_stack = []

        # set the count to 1 for creating the maze
        count = 0

        while count < self.num_rooms:
            adjacent_squares = self.get_adjacent_squares(current_square)

            # if there are no adjacent squares
            if not adjacent_squares:
                # remove from stack
                current_square = square_stack.pop()
                continue

            # Select an adjacent square
            direction, next_square = random.choice(adjacent_squares)
            # remove the sides of the squares to join them together
            current_square.connect_squares(next_square, direction)
            current_square.set_connecting_square(next_square, direction)
            next_square.outstanding = False
            # add the current square to the stack
            square_stack.append(current_square)
            # move to the next square
            current_square = next_square
            # increment the count for next room
            count += 1

maze = Maze(30, 10)
maze.create_maze()

print(maze)

# test_square = Square(1,1)

# print('\n',test_square.sides['up'])
# print(test_square.sides['down'])
# print(test_square.sides['left'])
# print(test_square.sides['right'])
# print('\n',test_square.has_all_sides())
# test_square.sides['down'] = False
# print('',test_square.has_all_sides())
# test_square.id = 55
# print('\n',test_square.sides['up'])
# print(test_square.sides['down'])
# print(test_square.sides['left'])
# print(test_square.sides['right'])

# print(test_square)

print('up: ', maze.maze_map[1][1].up_to)
print('down: ', maze.maze_map[1][1].down_to)
print('left: ', maze.maze_map[1][1].left_to)
print('right: ', maze.maze_map[1][1].right_to)