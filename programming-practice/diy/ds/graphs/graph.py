from collections import defaultdict

# Todo: detect loop in a graph
# Todo: Complete the remaining bare implementations here
# Todo: Graph coloring problem


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

    def get_edges(self, vertex):
        return self.graph.get(vertex)

    def vertices(self):
        return list(self.graph.keys())

    def bfs(self):
        visited = defaultdict(lambda: False)
        queue = [self.vertices()[0]]

        while len(queue) > 0:
            v = queue.pop(0)

            if not visited[v]:
                print(v)
                visited[v] = True

                edges = self.get_edges(v)

                if not edges:
                    continue

                for edge in edges:
                    if not visited[edge]:
                        queue.append(edge)

    def dfs(self, start, visited):
        visited[start] = True
        print(start)

        for edge in self.graph[start]:
            if not visited.get(edge):
                self.dfs(edge, visited)

    def topological_sort(self):
        # DAG
        pass

    def __str__(self):
        return f'{self.graph}'


def construct_graph():
    g = Graph()
    g.add(1, 2)
    g.add(1, 3)
    g.add(2, 4)
    g.add(2, 3)
    g.add(3, 4)

    return g


def construct_graph_2():
    g = Graph()
    g.add(0, 1)
    g.add(0, 2)
    g.add(1, 2)
    g.add(2, 0)
    g.add(2, 3)
    g.add(3, 3)
    return g


def main():
    graph = construct_graph()

    graph.bfs()

    construct_graph_2().dfs(1, {})


if __name__ == '__main__':
    main()



