# A BST based implementation of a set
# ==> no duplicate elements
# The implementation has two parts:
# - class AvlSet   (Provided! No need to modify!)
# - class AvlSet  (Not complete ==> add missing code)


class AvlNode:
    def __init__(self, value, left, right, height=1):
        self.value = value
        self.left = left
        self.right = right
        self.height = height

    def __str__(self):
        txt = ""
        if self.left is not None:
            txt += self.left.__str__()
        txt += str(self.value) + " "
        if self.right is not None:
            txt += self.right.__str__()
        return txt

    def add(self, val):
        if val < self.value: # No duplicates
            if self.left is None:
                self.left = AvlNode(val, None, None)  # Add new node
            else:
                self.left = self.left.add(val)  # Update left child after rebalancing
        elif val > self.value: # No duplicates
            if self.right is None: 
                self.right = AvlNode(val, None, None) # Add new node
            else: 
                self.right = self.right.add(val) # Update right child after rebalancing

        # Update height
        self.height = 1 + max(self.get_height(self.left), self.get_height(self.right))  

        # Rebalance the node if needed
        return self.rebalance()

    def delete(self, val, parent=None):
        if val < self.value:
            if self.left:
                self.left = self.left.delete(val, self)
        elif val > self.value:
            if self.right:
                self.right = self.right.delete(val, self)
        else:
            # Node with one or no child
            if not self.left:
                return self.right
            elif not self.right:
                return self.left

            # Node with two children
            min_larger_node = self.right.find_min()
            self.value = min_larger_node.value
            self.right = self.right.delete(min_larger_node.value, self)

        # Update height
        self.height = 1 + max(self.get_height(self.left), self.get_height(self.right))

        # Rebalance the node
        return self.rebalance()

    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self):
        return self.get_height(self.left) - self.get_height(self.right)

    def rotate_left(self):
        new_root = self.right
        self.right = new_root.left
        new_root.left = self

        self.height = 1 + max(self.get_height(self.left), self.get_height(self.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))

        return new_root

    def rotate_right(self):
        new_root = self.left
        self.left = new_root.right
        new_root.right = self

        self.height = 1 + max(self.get_height(self.left), self.get_height(self.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))

        return new_root

    def rebalance(self): # height of right child − height of left child
        balance = self.get_balance()

        if balance > 1:  # Left heavy
            if self.left.get_balance() < 0:
                self.left = self.left.rotate_left()
            return self.rotate_right()

        if balance < -1:  # Right heavy
            if self.right.get_balance() > 0:
                self.right = self.right.rotate_right()
            return self.rotate_left()

        return self

    def find_min(self):
        return self.left.find_min() if self.left else self

    def max_depth(self):
        left_depth = self.left.max_depth() if self.left else 0
        right_depth = self.right.max_depth() if self.right else 0
        return 1 + max(left_depth, right_depth)

    def dot(self, parent=None):
        result = ""
        if parent is not None:
            result += f"{parent} -- {self.value} [label=\"h={self.height}, b={self.get_balance()}\"];\n"
        if self.left:
            result += self.left.dot(self.value)
        if self.right:
            result += self.right.dot(self.value)
        return result

#
# The class AvlSet
#
class AvlSet:
    def __init__(self):
        self.root = None

    def add(self, val):
        if self.root is None:
            self.root = AvlNode(val, None, None)
        else:
            self.root = self.root.add(val)  # Update root after rebalancing

    def delete(self, val):
        if self.root is None:
            return False
        self.root = self.root.delete(val, None)  # Update root after deletion
        return True

    def __str__(self):
        txt = "{ "
        if self.root is not None:
            txt += self.root.__str__()
        return txt + "}"

    def max_depth(self):
        return self.root.max_depth() if self.root else 0

    def dot(self):
        if self.root is None:
            return "No nodes ==> no graph markup"
        else:
            dot_text = "graph BST {\n"
            dot_text += self.root.dot(None)  # None as parent
            dot_text += "}"
            return dot_text
