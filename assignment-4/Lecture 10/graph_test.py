from Graph import Graph

# Create vertices and edges
vertices = ["A", "B", "C", "D"]
edges = [
    [0, 1],  # A -> B
    [0, 2],  # A -> C
    [1, 3],  # B -> D
    [2, 3]   # C -> D
]

# Create a graph
graph = Graph(vertices, edges)

# Add a new vertex and edge
graph.addVertex("E")
graph.addEdge(graph.getIndex("A"), graph.getIndex("E"))  # A -> E

# Test methods
print("Vertices:", graph.getVertices())  # Should print: ['A', 'B', 'C', 'D', 'E']
print("Size of graph:", graph.getSize())  # Should print: 5
print("Degree of A:", graph.getDegree("A"))  # Should print: 3 (B, C, E are neighbors)
print("Adjacency Lists:", graph.adjacencyLists)  # Should reflect all connections
