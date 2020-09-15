
# Function to reverse path
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
# traversal thru as an arr list stack [[0]]
# make cache to store key and value dictionary pair {player room id: {player exits[n]: '?'}}

# make a function that
