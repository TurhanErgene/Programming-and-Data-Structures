import AvlSet as avl

avl_tree = avl.AvlSet()

# Adding values 1-20
for i in range(1, 21):
    avl_tree.add(i)
print("DOT after adding 1-20:")
print(avl_tree.dot())

# Deleting values 1-10
for i in range(1, 11):
    avl_tree.delete(i)
print("DOT after deleting 1-10:")
print(avl_tree.dot())