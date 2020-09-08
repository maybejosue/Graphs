"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            print("Vertex does not exist")

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        q = Queue()
        q.enqueue(starting_vertex)

        visited = set()

        while q.size() > 0:
            a_vertex = q.dequeue()

            if a_vertex not in visited:
                visited.add(a_vertex)
                print(a_vertex)

                for next_vertex in self.get_neighbors(a_vertex):
                    q.enqueue(next_vertex)

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

    def dft_recursive(self, starting_vertex, visited=None):
        s = Stack()
        s.push(starting_vertex)

        if visited is None:
            visited = set()

        if s.size() > 0:
            a_vertex = s.pop()

            if a_vertex not in visited:
                visited.add(a_vertex)
                print(a_vertex)

                for next_vertex in self.get_neighbors(a_vertex):
                    s.push(next_vertex)

                self.dft_recursive(s.pop(), visited)

    def bfs(self, starting_vertex, destination_vertex):
        q = Queue()
        q.enqueue([starting_vertex])

        visited = set()

        while q.size() > 0:
            path = q.dequeue()
            v = path[-1]

            if v not in visited:
                if v == destination_vertex:
                    return path

                visited.add(v)

                for next_v in self.get_neighbors(v):
                    path_copy = list(path)
                    path_copy.append(next_v)
                    q.enqueue(path_copy)

        return None

    def dfs(self, starting_vertex, destination_vertex):
        s = Stack()
        s.push([starting_vertex])

        visited = set()

        while s.size() > 0:
            path = s.pop()
            v = path[-1]

            if v not in visited:
                if v == destination_vertex:
                    return path

                visited.add(v)

                for next_v in self.get_neighbors(v):
                    path_copy = list(path)
                    path_copy.append(next_v)
                    s.push(path_copy)

        return None

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):

        if visited is None:
            visited = set()

        if path is None:
            path = list()

        visited.add(starting_vertex)
        path = path + [starting_vertex]

        if starting_vertex == destination_vertex:
            return path

        for next_v in self.get_neighbors(starting_vertex):
            if next_v not in visited:
                new_path = self.dfs_recursive(
                    next_v, destination_vertex, visited, path)
                if new_path:
                    return new_path

        return None


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
