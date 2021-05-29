# Refer: https://www.youtube.com/watch?v=4ZlRH0eK-qQ
import heapq
from collections import defaultdict


class KruskalMinimumSpanningTree:
    graph = defaultdict(list)

    def __init__(self, n):
        self.n = n + 1
        self.actual_length = n
        self.parent = [i for i in range(self.n)]

    def heapify_graph(self):
        queue = []
        for vertex in range(self.n):
            for edge in self.graph[vertex]:
                heapq.heappush(queue, [edge, vertex])

        return queue

    def find(self, i):
        if self.parent[i] == i:
            return i
        return self.find(self.parent[i])

    def find_minimum_spanning_tree(self):
        min_spanning_tree = []
        cost = 0
        queue = self.heapify_graph()

        while queue:
            edge_node, node = heapq.heappop(queue)
            if not edge_node:
                continue
            weight = edge_node[0]
            edge = edge_node[1]
            parent_of_edge = self.find(edge)
            parent_of_node = self.find(node)
            if parent_of_edge != parent_of_node:
                cost += weight
                min_spanning_tree.append([node, edge])
                self.parent[parent_of_edge] = parent_of_node

        return min_spanning_tree, cost


if __name__ == '__main__':
    kruskal = KruskalMinimumSpanningTree(7)
    kruskal.graph[1].append([10, 6])
    kruskal.graph[1].append([28, 2])
    kruskal.graph[2].append([14, 7])
    kruskal.graph[2].append([16, 3])
    kruskal.graph[3].append([12, 4])
    kruskal.graph[4].append([18, 7])
    kruskal.graph[4].append([22, 5])
    kruskal.graph[5].append([25, 6])
    kruskal.graph[5].append([24, 7])
    kruskal.graph[6].append([])
    kruskal.graph[7].append([])

    print(kruskal.find_minimum_spanning_tree())
