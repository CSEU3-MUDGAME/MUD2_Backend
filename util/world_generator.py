from util.maze_generator import Maze
from adventure.models import Room

maze = Maze(25, 30)
maze.create_maze()

for array in maze.maze_map:
    for square in array:
        roomNo = square.id
        game_exit = square.game_exit
        n_to = square.up_to
        s_to = square.down_to
        e_to = square.right_to
        w_to = square.left_to
        up = square.up_to != -1
        down = square.down_to != -1
        left = square.left_to != -1
        right = square.right_to != -1
        items = "".join(square.contents)
        new_room = Room(id=roomNo, n_to=n_to, s_to=s_to, e_to=e_to, w_to=w_to,
                        up=up, down=down, left=left, right=right, items=items, game_exit=game_exit)
        new_room.save()

print('done')