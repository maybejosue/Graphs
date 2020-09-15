from room import Room
from player import Player
from world import World
from util import Queue, Stack

import random
from ast import literal_eval


# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# # Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)
print(
    f'player room id: {player.current_room.id}, player exists: {player.current_room.get_exits()} ')

# Function to reverse path

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

###### MY CODE STARTS HERE ######

# function to set room directions as '?'


def get_directions():
    for new_exit in player.current_room.get_exits():
        rooms[player.current_room.id][new_exit] = '?'

# function to grab random direction


def random_direction(room_id):
    for direction in rooms[room_id]:
        if rooms[room_id][direction] == '?':
            return direction

    visited.pop()
    for new_direction, room_num in rooms[visited[-1]].items():
        if room_num == room_id:
            return inverse_directions[new_direction]


# Initialize empty data structure
rooms = dict()
visited = list()
path = list()
inverse_directions = {'n': 's', 's': 'n', 'w': 'e', 'e': 'w'}


# Fill data structure with starting room
visited.append(player.current_room.id)
path.append(player.current_room.id)
rooms[player.current_room.id] = dict()
get_directions()

print(rooms)
while len(rooms) < len(world.rooms):
    # move to the nearest empty direction
    move = random_direction(player.current_room.id)
    # move player to nearest direction and append direction to traversal_path
    player.travel(move)
    traversal_path.append(move)

    # if current room not the same as the previous room
    if player.current_room.id is not visited[-1]:
        # append current room to visited and path
        visited.append(player.current_room.id)
        path.append(player.current_room.id)
    # if current room not in rooms dictionary
    if player.current_room.id not in rooms.keys():
        # add the room to rooms instance and set value as an empty dictionary
        rooms[player.current_room.id] = dict()
        get_directions()
    # set current room direction value and room
    if rooms[player.current_room.id][inverse_directions[move]] == '?':
        rooms[visited[-2]][move] = player.current_room.id
        rooms[player.current_room.id][inverse_directions[move]] = visited[-2]

###### CODE ENDS HERE ######
print(rooms)


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
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
