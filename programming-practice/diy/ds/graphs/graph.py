from collections import defaultdict


class Graph:

    def __init__(self, directed=True):
        self.graph = defaultdict(list)
        self.directed = directed

    def add(self, u, v):
        self.graph[u].append(v)

        if not self.directed:
            self.graph[v].append(u)

    def print(self):
        for vertex, edges in self.graph.items():
            for edge in edges:
                print(vertex, edge)


def main():
    g = Graph()
    g.add(1, 2)
    g.add(1, 3)
    g.add(2, 4)
    g.add(2, 3)
    g.add(3, 4)

    g.print()


if __name__ == '__main__':
    main()




