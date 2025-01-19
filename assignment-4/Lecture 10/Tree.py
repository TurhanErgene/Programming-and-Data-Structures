class Tree:
    def __init__(self, root, parent, searchOrders, vertices):
        self.root = root  # The root of the tree
        self.parent = parent  # Parent list (index-based)
        self.searchOrders = searchOrders  # Order in which vertices were visited
        self.vertices = vertices  # List of vertices

    # Return the root of the tree
    def getRoot(self):
        return self.root

    # Return the parent of vertex v
    def getParent(self, index):
        return self.parent[index]

    # Return an array representing search order
    def getSearchOrders(self):
        return self.searchOrders

    # Return number of vertices found
    def getNumberOfVerticesFound(self):
        return len(self.searchOrders)

    # Return the path of vertices from a vertex index to the root
    def getPath(self, index):
        path = []
        while index != -1: # if not root
            path.append(self.vertices[index]) # adad current vertex to the path
            index = self.parent[index] # move to the parent
        return path[::-1] # reverse to get path from root to vertex

    # Print a path from the root to vertex v
    def printPath(self, index):
        path = self.getPath(index)
        print(" -> ".join(path))  # Print the path in a readable format

    # Print the whole tree
    def printTree(self):
        print(f"Root: {self.vertices[self.root]}")
        for i in range(len(self.parent)):
            if self.parent[i] != -1:  # If the vertex has a parent
                print(f"Parent of {self.vertices[i]} is {self.vertices[self.parent[i]]}")


# root = 0  # Assume the root is vertex 0 (e.g., "A")
# parent = [-1, 0, 0, 1, 0]  # Parent-child relationships
# searchOrders = [0, 1, 3, 2, 4]  # DFS order
# vertices = ["A", "B", "C", "D", "E"]  # List of vertices

# tree = Tree(root, parent, searchOrders, vertices)

# print("Root:", tree.getRoot())  # Should print: 0
# print("Search Orders:", tree.getSearchOrders())  # Should print: [0, 1, 3, 2, 4]
# print("Parent of D:", tree.getParent(3))  # Should print: 1 (B is parent of D)
# print("Number of Vertices Found:", tree.getNumberOfVerticesFound())  # Should print: 5
# print("Path to D:", tree.getPath(3))  # Should print: ['A', 'B', 'D']
# print("Path to E:")
# tree.printPath(4)  # Should print: A -> E
# print("Tree Structure:")
# tree.printTree()