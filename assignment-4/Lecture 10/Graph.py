from Tree import Tree
from Queue import Queue


class Graph:
    def __init__(self, vertices=[], edges=[]):
        self.vertices = vertices
        self.edges = edges

        # "neighbors"
        self.adjacencyLists = self.getAdjacencyLists(edges)

    # Return a list of adjacency lists for edges
    def getAdjacencyLists(self, edges):
        adjacencyLists = [[] for _ in range(len(self.vertices))]
        for edge in edges:
            # u, v = edge[0], edge[1]
            u, v = edge
            adjacencyLists[u].append(v)
        return adjacencyLists

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
        return len(self.adjacencyLists[self.getIndex(v)])

    # Print the edges
    def printEdges(self):
        pass

    # Clear graph
    def clear(self):
        pass

    def addVertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices.append(vertex)
            self.adjacencyLists.append([])

    def addEdge(self, u, v):
        # Ensure u and v are strings (vertices) if needed
        if isinstance(u, int):
            u = self.vertices[u]
        if isinstance(v, int):
            v = self.vertices[v]

        # Add vertices if they do not exist
        if u not in self.vertices:
            self.addVertex(u)
        if v not in self.vertices:
            self.addVertex(v)  

        # get the neighbors of u and add v to the list if it's not already there
        self.adjacencyLists[self.getIndex(u)].append(self.getIndex(v))



    # Obtain a DFS tree starting from vertex v
    def dfs(self, v):
        pass

    # Recursive method for DFS search
    def dfsHelper(self, v, parent, searchOrders, isVisited):
        pass

    # Starting bfs search from vertex v
    def bfs(self, v):
        pass


class Edge:
    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        # self.weight = weight

    # in weighted graph, we can compare edges by their weights
    # def __lt__(self, other):
    #     return self.weight < other.weight
