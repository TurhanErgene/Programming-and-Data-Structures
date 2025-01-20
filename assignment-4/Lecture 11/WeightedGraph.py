from Graph import Graph
from Tree import Tree
from WeightedEdge import WeightedEdge
from Queue import Queue


class WeightedGraph(Graph):
    def __init__(self, vertices=[], edges=[]):
        super().__init__(vertices, edges)

    # Pseudocode for Adjacency List method (You need to write the code)
    def getAdjacencyLists(self, edges):
        self.neighbors = [
            [] for _ in range(len(self.vertices))
        ]  # Initialize empty lists for each vertex
        for u, v, w in edges:  # Iterate over each edge with its weight
            self.neighbors[u].append(
                WeightedEdge(u, v, w)
            )  # Add a directed weighted edge
        return self.neighbors

    # Display edges with weights
    def printWeightedEdges(self):
        for u in range(len(self.neighbors)):
            print(f"Vertex {self.vertices[u]}: ", end="")
            for edge in self.neighbors[u]:
                print(
                    f"({self.vertices[edge.u]}, {self.vertices[edge.v]}, {edge.weight})",
                    end=" ",
                )
            print()  # New line for each vertex

    # Return the weight between two vertices
    def getWeight(self, u, v):
        for edge in self.neighbors[u]:  # Iterate over all neighbors of vertex u
            if edge.v == v:  # Check if the neighbor matches vertex v
                return edge.weight
        return None  # Return None if no edge exists between u and v

    # Override the addEdge method to add a weighted edge
    def addEdge(self, u, v, w):
        self.neighbors[u].append(WeightedEdge(u, v, w))  # Add the edge with its weights

    # Get a minimum spanning tree rooted at the specified vertex
    def getMinimumSpanningTree(self, startingVertex=0):
        visited = [False] * len(self.vertices)  # Track visited vertices
        edge_queue = Queue()  # Use your Queue implementation for edge processing
        mst_edges = []  # Store edges in the MST
        total_weight = 0  # Total weight of the MST

        def visit(vertex):
            visited[vertex] = True  # Mark the vertex as visited
            # Add all unvisited neighbors to the queue
            for edge in self.neighbors[vertex]:
                if not visited[edge.v]:
                    edge_queue.enqueue((edge.weight, edge.u, edge.v))

        visit(startingVertex)

        while not edge_queue.isEmpty():
            weight, u, v = edge_queue.dequeue()  # Extract the smallest edge
            if visited[v]:
                continue  # Skip if the vertex is already in MST
            mst_edges.append((u, v, weight))  # Add the edge to MST
            total_weight += weight  # Update total weight
            visit(v)  # Visit the new vertex

        return MST(startingVertex, None, mst_edges, total_weight, self.vertices)

    # Find single source shortest paths
    def getShortestPath(self, sourceVertex):
        distances = [float("inf")] * len(
            self.vertices
        )  # Initialize distances to infinity
        parent = [-1] * len(self.vertices)  # Store the shortest-path tree
        distances[sourceVertex] = 0  # Distance to source is zero
        pq = Queue()  # Use your Queue implementation as a priority queue
        pq.enqueue((0, sourceVertex))  # Enqueue (distance, vertex)

        while not pq.isEmpty():
            current_distance, current_vertex = pq.dequeue()
            # Skip if we already found a shorter path
            if current_distance > distances[current_vertex]:
                continue

            for edge in self.neighbors[current_vertex]:
                neighbor = edge.v
                # Calculate new distance via current_vertex
                new_distance = current_distance + edge.weight
                if new_distance < distances[neighbor]:  # check for improvement
                    distances[neighbor] = new_distance
                    parent[neighbor] = current_vertex  # Update parent in the path
                    pq.enqueue((new_distance, neighbor))  # Enqueue updated distance

        return ShortestPathTree(sourceVertex, parent, distances, self.vertices)


# MST is a subclass of Tree which you have implemented it in the preceding assignment
class MST(Tree):
    def __init__(self, startingIndex, parent, T, totalWeight, vertices):
        super().__init__(startingIndex, parent, T, vertices)
        self.totalWeight = totalWeight  # Store the total weight of the MST

    def getTotalWeight(self):
        # Return the total weight of the MST
        return self.totalWeight


class ShortestPathTree(Tree):
    def __init__(self, sourceIndex, parent, T, costs, vertices):
        super().__init__(sourceIndex, parent, T, vertices)
        self.costs = costs  # Store the cost from source to each vertex

    # Return the cost for a path from the root to vertex v
    def getCost(self, v):
        return self.costs[v]  # Return the precomputed cost to vertex v

    # Print paths from all vertices to the source
    def printAllPaths(self):
        print(f"Paths from the source vertex {self.vertices[self.root]}:")
        for i in range(len(self.vertices)):
            if self.costs[i] < float("inf"):  # Check if vertex is reachable
                print(f"Path to {self.vertices[i]} (cost {self.costs[i]}): ", end="")
                self.printPath(i)  # Print the path using the Tree method
            else:
                print(f"{self.vertices[i]} is unreachable.")
