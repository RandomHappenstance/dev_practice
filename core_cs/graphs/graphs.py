from collections import defaultdict
from collections import deque

class Graph:
    def __init__(self, graph: None):
        if graph is None:
            graph = defaultdict(list)
        self.__graph = graph

    def vertices(self):
        """ Essential. """
        return list(self.__graph.keys())

    def edges(self):
        """ Essential. """
        return self.__generate_edges()

    def add_vertex(self, vertex):
        """ Essential. """

        if vertex not in self.__graph.keys():
            self.__graph[vertex] = []

    def add_edge(self, edge):
        """ Essential. """
        self.__graph[edge[0]].append(edge[1])

    def __generate_edges(self):
        """ Essential. """
        edges = []
        for vertex in self.__graph.keys():
            for neighbor in self.__graph[vertex]:
                if [vertex, neighbor] not in edges:
                    edges.append([vertex, neighbor])
        return edges

    def bsf(self, initial):

        visited = []

        queue = [initial]

        while queue:
            node = queue.pop()
            # if node == goal:
            #     return self.__graph[node]
            if node not in visited:
                print(node)
                visited.append(node)
                neighbors = self.__graph[node]

                for neighbor in neighbors:
                    queue.append(neighbor)
        return None

    def bsf_rec(self, initial, goal):
        visited = []
        queue = [initial]
        return self._bfs_rec(self.__graph, queue, visited, goal)

    def _bsf_rec(self, graph, queue, visited, goal):

        if not queue:
            return

        node = queue.pop()
        if node == goal:
            return graph[node]

        if node not in visited:
            visited.append(node)
            print(node)

            neighbors = graph[node]
            for neighbor in neighbors:
                if neighbor not in visited:
                    visited.append(neighbor)
                    queue.append(neighbor)
                    self._bfs_rec(graph, queue, visited, goal)

#         - 4
#    -  2 - 5
# 1     |
#   -  3  - 6
#         - 7
#         - 8

    def dfs(self, initial):
        """ Essential. """
        visited = []
        queue = deque()
        queue.append(initial)
        self._dfs(visited, queue)

    def _dfs(self, visited, queue):
        if queue:
            node = queue.pop()

            # if node == goal:
            #     return True
            if node not in visited:
                visited.append(node)

            print(node)

            neighbors = self.__graph[node]
            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)
                self._dfs(visited, queue)
        return False

    def height(self):
        return self._height()

    def _height(self, node):

    def __str__(self):
        pass

    def find_path(self):
        pass

    def find_all_paths(self):
        pass

    def find_isolated_vertices(self):
        pass

    def is_connected(self):
        pass

    def vertex_degree(self):
        pass

    def degree_sequence(self):
        pass

    def is_degree_sequence(self):
        pass

    def degree(self):
        pass

    def Degree(self):
        pass

    def density(self):
        pass

    def diameter(self):
        pass


if __name__ == "__main__":
    g = {"a": ["d", "g", "f"],
         "b": ["c"],
         "c": ["b", "d", "e"],
         "d": ["a", "c"],
         "e": ["c"],
         "f": ["a"],
         "g": ["a", "h", "i"],
         "h": ["g"],
         "i": ["g"]}

    gd = Graph(g)
    # print(gd.edges())

    # print(gd)

    gd.dfs('a')
