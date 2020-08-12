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


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("You can't do that, bud.")


def earliest_ancestor(ancestors, starting_node):
    # initiate the graph
    g = Graph()
    # loop thru the ancestors array to build graph in memeory (i.e. using edges to connect the vertex)
    for pair in ancestors:
        # create vertex for both item in the tuple
        g.add_vertex(pair[0])
        g.add_vertex(pair[1])
        # connect the vertex to each other via edge
        g.add_edge(pair[1], pair[0])

    # initiate a stack
    s = Stack()
    # push starting node as a list into the stack
    s.push([starting_node])
    pathMax = 1
    # we assume the ancestor does not exist so we initialize it via -1
    ancestor = -1
    # keeps looping while size of stack is greater than 0
    while s.size() > 0:
        print(f'stack: {s.stack}')
        # the array is popped out of the stack
        path = s.pop()
        print(f"pathMax: {pathMax}, ancestor: {ancestor}, stack: {s.stack}")
        # gets the last number out of the array it popped out
        v = path[-1]
        print(f'path:{path}, vertex: {v}')
        if (len(path) >= pathMax and v < ancestor) or (len(path) > pathMax):
            # override the earliest ancestor
            ancestor = v
            pathMax = len(path)
            print(f"answer? {ancestor}, pathmax? {pathMax}")
        for n in g.vertices[v]:
            tempPath = list(path)
            print(f'tempPath: {tempPath}')
            tempPath.append(n)
            s.push(tempPath)
    return ancestor
