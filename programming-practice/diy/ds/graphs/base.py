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
