
from Tree import Tree
from Queue import Queue


class Graph:
    def __init__(self, vertices = [], edges = []):
        self.vertices = vertices
        self.edges = edges
        pass

    # Return a list of adjacency lists for edges
    def getAdjacencyLists(self, edges):
        pass

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
    def getDegree(self, v):
        pass

    # Print the edges
    def printEdges(self):
        pass

    # Clear graph
    def clear(self):
        pass
     
    def addVertex(self, vertex):
        pass
   
    def addEdge(self, u, v):
        pass



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
    def __init__(self, u, v):
        pass