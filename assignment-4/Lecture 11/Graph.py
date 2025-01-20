from Tree import Tree
from Queue import Queue


class Graph:
    def __init__(self, vertices=[], edges=[]):
        self.vertices = vertices
        # self.edges = edges

        # "neighbors"
        self.neighbors = self.getAdjacencyLists(edges)

    # Return a list of adjacency lists for edges
    def getAdjacencyLists(self, edges):
        neighbors = []
        for vertex in range(len(self.vertices)):
            neighbors.append([])  # Each vertex has an empty list of neighbors
        for i in range(len(edges)):
            # Each edge in the edges list is a pair of vertices (two numbers).
            u = edges[i][0]  # gets the starting vertex of the edge.
            v = edges[i][1]  # gets the ending vertex of the edge.
            neighbors[u].append(Edge(u, v))  # Insert an edge (u,v)
        return neighbors

    # Return the number of vertices in the graph
    def getSize(self):
        return len(self.vertices)

    # Return the vertices in the graph
    def getVertices(self):
        return self.vertices

    # Return the vertex at the specified index
    def getVertex(self, index):
        return self.vertices[index]

    # Return the index for the specified vertex
    def getIndex(self, v):
        return self.vertices.index(v)

    # Return the neighbors of vertex with the specified index
    def getNeighbors(self, index):
        return self.edges[index]

    # Return the degree for a specified vertex
    # The degree of a vertex is the number of edges connected to it
    def getDegree(self, v):
        return len(self.neighbors[self.getIndex(v)])

    # Print the edges
    def printEdges(self):
        for u in range(len(self.neighbors)):
            print(f"Vertex {self.vertices[u]}: ", end="")
            for edge in self.neighbors[u]:
                print(f"({self.vertices[edge.u]}, {self.vertices[edge.v]})", end=" ")
            print()  # Newline for the next vertex

    # Clear graph
    def clear(self):
        self.vertices = []
        self.edges = []

    def addVertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices.append(vertex)
            self.neighbors.append([])

    def addEdge(self, u, v):
        # Ensure u and v are vertex indices
        if isinstance(u, int):
            u = self.vertices[u]
        if isinstance(v, int):
            v = self.vertices[v]

        # Add vertices if they do not exist
        if u not in self.vertices:
            self.addVertex(u)
        if v not in self.vertices:
            self.addVertex(v)

        # Append an Edge object to the adjacency list
        self.neighbors[self.getIndex(u)].append(
            Edge(self.getIndex(u), self.getIndex(v))
        )

    # Obtain a DFS tree starting from vertex v
    def dfs(self, v):
        searchOrders = []  # keeps track of the order in which vertices are visited
        parent = [-1] * len(
            self.vertices
        )  # tracks the parent of each vertex in the dfs tree
        isVisited = [False] * len(self.vertices)

        self.dfsHelper(v, parent, searchOrders, isVisited)

        return Tree(v, parent, searchOrders, self.vertices)

    # Recursive method for DFS search
    def dfsHelper(self, v, parent, searchOrders, isVisited):
        # Mark the current vertex as visited
        isVisited[v] = True
        searchOrders.append(v)

        # Visit each neighbor of the current vertex
        for edge in self.neighbors[v]:  # Each neighbor is an Edge object
            neighbor = edge.v  # Extract the destination vertex from the Edge
            if not isVisited[neighbor]:  # If the neighbor is not visited
                parent[neighbor] = v  # Set the current vertex as the parent
                self.dfsHelper(neighbor, parent, searchOrders, isVisited)

    # Starting bfs search from vertex v  # 33(34)
    def bfs(self, v):
        searchOrders = []  # To track the order in which vertices are visited
        parent = [-1] * len(self.vertices)  # Tracks the parent of each vertex
        isVisited = [False] * len(
            self.vertices
        )  # Tracks whether a vertex has been visited

        """ create an empty queue for storing vertices to be visited
            add v into the queue
            mark v visited """
        queue = Queue()
        queue.enqueue(v)  # start with the given vertex
        isVisited[v] = True

        while not queue.isEmpty():
            current = queue.dequeue()  # Visit the vertex at the front of the queue
            searchOrders.append(current)

            # Visit all neighbors of the current vertex
            for edge in self.neighbors[current]:
                neighbor = edge.v  # Get the neighbor from the Edge object
                if not isVisited[neighbor]:  # If the neighbor hasn't been visited
                    queue.enqueue(neighbor)  # Add it to the queue
                    parent[neighbor] = (
                        current  # Record the current vertex as its parent
                    )
                    isVisited[neighbor] = True  # Mark it as visited

        # Return a Tree object for the BFS traversal
        return Tree(v, parent, searchOrders, self.vertices)


class Edge:
    def __init__(self, u, v):
        self.u = u
        self.v = v
