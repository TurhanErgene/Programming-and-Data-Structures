# A BST based implementation of a set 
# ==> no duplicate elements
# The implementation has two parts:
# - class BstSet   (Provided! No need to modify!)
# - class BstNode  (Not complete ==> add missing code)

class BstNode:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

    def add(self, val):
        if val < self.value:
            if self.left is None:
                self.left = BstNode(val, None, None)
            else:
                self.left.add(val)
        elif val > self.value:
            if self.right is None:
                self.right = BstNode(val, None, None)
            else:
                self.right.add(val)

    def __str__(self):
        txt = ""
        if self.left is not None:
            txt += self.left.__str__()
        txt += str(self.value) + " "
        if self.right is not None:
            txt += self.right.__str__()
        return txt

    def search(self, val):
        if val == self.value:
            return True
        elif val < self.value:
            if self.left is None:
                return False
            else:
                return self.left.search(val)
        else:
            if self.right is None:
                return False
            else:
                return self.right.search(val)
            

    def count(self):
        left_count = self.left.count() if self.left else 0
        right_count = self.right.count() if self.right else 0
        return 1 + left_count + right_count


    def count_internal(self):
    # Base case: leaf node or None
        if self.left is None and self.right is None:
            return 0
            
        left_count = self.left.count_internal() if self.left else 0
        right_count = self.right.count_internal() if self.right else 0
        return 1 + left_count + right_count    
        

    def max_depth(self):
        if self is None:
            return 0
        
        left_depth = self.left.max_depth() if self.left else 0
        right_depth = self.right.max_depth() if self.right else 0

        return 1 + max(left_depth, right_depth)
        

    def lr_inorder(self, lst):
        pass

    def rl_postorder(self, lst):
        pass

    def dot(self, parent):
        pass

    # Find node X to be deleted
    # - Case 1: X with no left child ==> replace X with right child of X
    # - Case 2: X as a left child ==> find max in left subtree, 
    #           move max value to X and remove max node
    def delete(self, value, parent):
        pass

    # VG Exercise
    def pretty_dot(self, parent, id_count):
        pass


#
# The class BstSet
#
class BstSet:

    def __init__(self):
        self.root = None

    # Adds value val to tree (if it doesn't already exist)
    def add(self, val):
        if self.root is None:
            self.root = BstNode(val, None, None)
        else:
            self.root.add(val)

    # Returns a string representation of the tree values.
    # Sorted with smallest value first
    def __str__(self):
        txt = "{ "
        if self.root is not None:
            txt += self.root.__str__()
        return txt + "}"

    # Returns True if value val is stored in tree,
    # Otherwise False
    def search(self, val):
        if self.root is None:
            return False
        else:
            return self.root.search(val)

    # Count total number of nodes in the tree
    def size(self):
        if self.root is None:
            return 0
        else:
            return self.root.count()

    # Count number of internal nodes
    # ==> not including leafs
    def count_internal(self):
        if self.root is None:
            return 0
        else:
            return self.root.count_internal()
        
    # Number of nodes in longest root-to-leaf path
    def max_depth(self):
        if self.root is None:
            return 0
        else:
            return self.root.max_depth()

    # Returns a list of values in left-to-right post-order
    def lr_inorder(self):
        lst = []
        if self.root is not None:
            self.root.lr_inorder(lst)
        return lst

    # Returns a list of values in right-to-left post-order
    def rl_postorder(self):
        lst = []
        if self.root is not None:
            self.root.rl_postorder(lst)
        return lst

    # Delete a node with value val from tree. Returns True if succesful 
    # and False if value val doesn't exist in tree.
    # Extra care taken for removing the root. 
    def delete(self, val):
        if self.root is None:  # Empty tree
            return False

        if self.root.value == val:  # Delete root
            if self.root.left is None:
                if self.root.right is None:  # Delete singleton
                    self.root = None
                    return True
                else:      # Case 1 for root
                    self.root = self.root.right  # Bypass root
        return self.root.delete(val, None)

    # Returns a string representing a DOT markup of 
    # the BST suitable fror Graphvis Online.
    def dot(self):
        if self.root is None:
            return "No nodes ==> no graph markup"
        else:
            dot_text = "graph BST {\n"
            dot_text += self.root.dot(None)  # None as parent
            dot_text += "}"
            return dot_text

    #
    # VG Exercise
    #
    # As dot above but iy also inserts invisible nodes to make it possible 
    # to always identify a node as left or right child. See lecture slides.
    def pretty_dot(self):
        if self.root is None:
            return "No nodes ==> no graph markup"
        else:
            id_count = 0
            dot_text = "graph BST {\n"
            dot_text += self.root.pretty_dot(None, id_count)
            dot_text += "}"
            return dot_text




        

