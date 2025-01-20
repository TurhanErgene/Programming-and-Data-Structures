from WeightedGraph import WeightedGraph


def read_adjacency_list(file_path):
    adjacency_list = {}
    with open(file_path, "r") as file:
        for line in file:
            node, edges = line.strip().split(": ")
            edges = edges.split(", ")
            adjacency_list[node] = [
                (edge.split()[0], int(edge.split()[1])) for edge in edges
            ]
    return adjacency_list


# {'Lion': [('Tiger', 3), ('Elephant', 2), ('Zebra', 4)],...
def extract_vertices_and_edges(adjacency_list):
    vertices = list(adjacency_list.keys())  # Extract all unique vertices
    edges = []
    for node, neighbors in adjacency_list.items():
        for neighbor, weight in neighbors:
            # Convert node and neighbor to indices in the vertices list
            edges.append([vertices.index(node), vertices.index(neighbor), weight])
    return vertices, edges


# Assuming the file path is 'graph.txt'
adjacency_list = read_adjacency_list("graph.txt")
print(adjacency_list)
vertices, edges = extract_vertices_and_edges(adjacency_list)

graph = WeightedGraph(vertices, edges)
print("The number of vertices in the graph:", graph.getSize())
print("The vertex with index 1 is", graph.getVertex(1))
print("The edges for the graph:")
graph.printWeightedEdges()
