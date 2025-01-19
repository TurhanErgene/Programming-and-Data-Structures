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
print("Adjacency Lists:", graph.getAdjacencyLists)  # Should reflect all connections

# Print the edges
print("Initial Edges:")
graph.printEdges()

# Clear the graph
# graph.clear()
# print("\nGraph after clear:")
# print("Vertices:", graph.vertices)
# print("Adjacency Lists:", graph.adjacencyLists)

# Perform DFS starting from vertex A (index 0)
dfs_tree = graph.dfs(graph.getIndex("A"))
# Print the search order
print("DFS Order:", [graph.getVertex(i) for i in dfs_tree.getSearchOrders()])

# Perform BFS starting from vertex A (index 0)
bfs_tree = graph.bfs(graph.getIndex("A"))

# Print the BFS search order
print("BFS Order:", [graph.getVertex(i) for i in bfs_tree.getSearchOrders()])