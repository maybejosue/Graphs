from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
print(f'room_graph: {room_graph}')
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)
print(
    f'player room id: {player.current_room.id}, player exists: {player.current_room.get_exits()} ')

# Function to reverse path

###### MY CODE STARTS HERE ######


def retrace_path(path):

    original_position_directions = []
    inverse_path = {'n': 's', 'e': 'w', 's': 'n', 'w': 'e'}

    for direction in reversed(path):
        original_position_directions += inverse_path[direction]
    return path + original_position_directions


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


print(room_graph)


def dft(self, starting_vertex):
    s = Stack()
    s.push(starting_vertex)

    visited = set()

    while s.size() > 0:
        a_vertex = s.pop()

        if a_vertex not in visited:
            visited.add(a_vertex)
            print(a_vertex)

            for next_vertex in self.get_neighbors(a_vertex):
                s.push(next_vertex)


def touch_every_vertex(starting_vertex):
    pass

    ###### CODE ENDS HERE ######


    # Fill this out with directions to walk
    # traversal_path = ['n', 'n']
traversal_path = []


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


# ######
# UNCOMMENT TO WALK AROUND
# ######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
