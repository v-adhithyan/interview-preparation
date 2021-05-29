# Graphs

More than 50% real-world problem can be modelled using graphs. For complex problems
try to think it as a graph problem.

Most of the graph problems boils down to graph traversal and additional operation during traversal to solve the problem.

- Bread first traversal (BFS)
- Depth first traversal (DFS)

Trees are connected acyclic graphs. Directed Acyclic graphs (DAG) occurs in scheduling problem and also useful in topological sorting.

## Graph Representation

- Adjacency matrix
- Adjacency list

| Adjacency matrix | Adjacency list |
| ---------------- | -------------- |
| easier to check whether a edge is present | less memory for small graphs |
| less memory for large graphs | faster for traversal so better for most problems |
| easy insertion/deletion | faster to find degree of vertex |

## Breadth first traversal

- Uses queue to keep track of next nodes to visit.
- Time complexity:
- Space complexity: 

## Depth first traversal

- Uses stack to keep track of next nodes to visit. Recursion solves the problem of having explicit stack.
- Time complexity: O(V+E)
- Space complexity: O(V)

## Important problems

- Shortest path [Dijkstra]
- Graph coloring
- Loop detection
- Minimum spanning tree

## Additional notes to remember while solving graph problems

- All traversals use a visited array to keep track of nodes visited.
    - Only if a node is not visited, we should add the node to queue/stack for traversing later.
    - This applies that uses the traversal and additional operation.

## Shortest path notes

- Directed weighted graph [Dijkstra]
    - Calculates a shortest path from source node to every node.
    - For every unvisited node add the distance of that node with its edge
    - Only if the distance is shorter, it should be added to path and to queue for traversing later.
    - For every iteration node with shortest distance should be chosen. This can be achieved using min heap.

- Undirected graph [BFS]
    - Uses a visited array, distance array and previous array
    - previous array is used for backtracking to generate paths at the end.
    - Do a BFS.
    - If a node is not visited, traverse it's edges.
    - For each edge, if it is not visited increase the current node distance by 1 and assign it as distance of current edge and add it to queue for traversing later. In addition store the previous of current edge as current node. 

## Minimum spanning notes

- Undirected connected graph
- used in travelling salesman
- Prims and Kruskal algorithm

### Prims algorithm

- Select a start node.
- From the  start node, select the edge with minimum cost
- Then select adjacent edges with minimum cost.
- Implementation notes: Normal BFS
 
### Kruskal algorithm

- Always select a minimum cost edge
    - If it forms a cycle, discard and select from  other
    - If it does not form a cycle  add to remaining
- Time complexity is O(V*E) if V==E, then it is O(V^2)
- Since we always select a minimum node we can use a min heap to achieve the same. Now time complexity is O(V log E)
- Implementation notes: First heapify the input and do BFS on the heaped input

## Loop detection notes

- DFS can be used to find out loops. We can keep of  track of vertices in recursion stack. If we reach a node that is already in recursion stack, then there is a cycle.

## Graph coloring notes