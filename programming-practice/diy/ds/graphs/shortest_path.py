import math
import heapq
from collections import defaultdict


# shortest path using bfs
# https://www.freecodecamp.org/news/dijkstras-shortest-path-algorithm-visual-introduction/
# dijkstra is for weighted graph

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


class ShortestPathBFS(Graph):
    def bfs(self, start, dst, n, distance, previous):
        queue = []
        visited = [False for _ in range(n)]
        visited[start] = True
        queue.append(start)

        while queue:
            node = queue.pop(0)
            for edge in self.graph[node]:
                if not visited[edge]:
                    visited[edge] = True
                    queue.append(edge)
                    distance[edge] = distance[node] + 1
                    previous[edge] = node

                    if edge == dst:
                        return True

        return False

    def shortest_path(self, src, dst, n):
        distance = list()
        previous = list()
        for i in range(n):
            distance.append(0)
            previous.append(-1)
        has_shortest_path = self.bfs(src, dst, n, distance, previous)
        if has_shortest_path:
            path = [dst]
            crawl = dst

            while crawl != src:
                path.append(previous[crawl])
                crawl = previous[crawl]

            return True, distance[dst], path[::-1]
        else:
            return False, -1, []


class DijkstraShortestPath:
    graph = dict()

    def shortest_path(self, start, end):
        n = len(self.graph) + 1
        queue = []
        visited = [False] * n
        distances = [math.inf] * n
        path = [None] * n
        distances[start] = 0
        # from the remaining nodes that are to be visited, we need to select a node that has shortest distance
        # so using a min heap  here, which will always return a node with smallest distance
        heapq.heappush(queue, [distances[start], start])

        while queue:
            distance, node = heapq.heappop(queue)
            visited[node] = True
            if node == end:
                break
            for edge, weight in self.graph[node]:
                if not visited[edge]:
                    new_distance = distance + weight
                    if new_distance < distances[edge]:
                        distances[edge] = new_distance
                        path[edge] = node
                        heapq.heappush(queue, [new_distance, edge])

        return path, distances


def main():
    g = ShortestPathBFS()
    g.add(0, 1)
    g.add(0, 3)
    g.add(1, 2)
    g.add(3, 4)
    g.add(3, 7)
    g.add(4, 5)
    g.add(4, 6)
    g.add(5, 6)
    g.add(6, 7)

    has_shortest_path, shortest_path_distance, path = g.shortest_path(0, 7, 8)
    print(f'is there a shortest_path ? {has_shortest_path}')
    if has_shortest_path:
        print(f'shortest_path_distance {shortest_path_distance}')
        print(f'path {path}')

    g = DijkstraShortestPath()
    g.graph = defaultdict()
    g.graph[0] = [[1, 2], [2, 6]]
    g.graph[1] = [[3, 5]]
    g.graph[2] = [[3, 8]]
    g.graph[3] = [[4, 10], [5, 15]]
    g.graph[4] = [[5, 6], [6, 2]]
    g.graph[5] = [[6, 6]]
    g.graph[6] = []
    print(g.graph)
    print(g.shortest_path(0, 6))


if __name__ == '__main__':
    main()
