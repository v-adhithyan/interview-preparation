from collections import defaultdict


class TopologicalSort:
    graph = defaultdict(list)
    stack = list()

    def __init__(self, n):
        self.n = n

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def topological_sort_util(self, i, visited):
        visited.add(i)

        for edge in self.graph[i]:
            if edge not in visited:
                self.topological_sort_util(edge, visited)

        self.stack.insert(0, i)

    def topological_sort(self):
        visited = set()

        for i in range(0, self.n):
            if i not in visited:
                self.topological_sort_util(i, visited)

        return self.stack


if __name__ == '__main__':
    g1 = TopologicalSort(2)
    g1.add_edge(1, 0)

    print(g1.topological_sort())

    g2 = TopologicalSort(2)
    g2.add_edge(1, 0)
    g2.add_edge(0, 1)

    print(g2.topological_sort())
