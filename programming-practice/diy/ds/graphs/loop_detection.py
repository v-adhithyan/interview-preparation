from collections import defaultdict


class Graph:
    graph = defaultdict(list)

    def add(self, u, v):
        self.graph[u].append(v)

    def __str__(self):
        graph_repr = list()
        for u in self.graph.keys():
            for v in self.graph[u]:
                graph_repr.append(f'({u}, {v})')
        return '\n'.join(graph_repr)

    def __len__(self):
        return len(list(self.graph.keys()))


class LoopDetection(Graph):

    def dfs(self, start, visited, stack):
        visited[start] = True
        stack[start] = True

        for edge in self.graph[start]:
            if not visited[edge]:
                return self.dfs(edge, visited, stack)

            if stack[edge]:
                return True

        stack[start] = False
        return False

    def has_loop(self, start):
        n = len(self.graph) + 1
        visited = [False] * n
        stack = [False] * n
        return self.dfs(start, visited, stack)


# DFS returns True if loop exists
# Union Find can be used to find all nodes that form loop

class UnionFindLoopDetection:
    parents = {}

    def __init__(self, x):
        for i in range(x + 1):
            self.parents[i] = i

    def find(self, x):
        while self.parents[x] != x:
            self.parents[x] = self.parents[self.parents[x]]
            x = self.parents[x]

        return x

    def union(self, a, b):
        parent_a = self.find(a)
        parent_b = self.find(b)

        if parent_a != parent_b:
            self.parents[parent_b] = parent_a
            return True
        else:
            return False

    def detect_loop(self, edges):
        loops = []
        for a, b in edges:
            status = self.union(a, b)
            if not status:
                loops.append([a, b])

        return loops


if __name__ == '__main__':
    graph = LoopDetection()
    graph.add(0, 1)
    graph.add(0, 2)
    graph.add(1, 2)
    graph.add(2, 0)
    graph.add(2, 3)
    graph.add(3, 3)

    print(graph.has_loop(0))

    uf = UnionFindLoopDetection(4)
    print(uf.detect_loop([
        [0, 1],
        [0, 2],
        [1, 2],
        [2, 0],
        [2, 3],
        [3, 3]
    ]))
