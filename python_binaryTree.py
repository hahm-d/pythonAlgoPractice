# Trees are non-linear data structures that represent nodes connected by edges. 
# Each tree consists of a root node as the Parent node, and the left node and right node as Child nodes.

# Insert
# if the node is greater than the parent node, it is inserted as a right node; otherwise,​ it’s inserted left.

class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
    # Compare the new value with the parent node
        if self.data:
            print("data: {}".format(data), "self.data: {}".format(self.data))
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)  
                print("inserted left: {}".format(data))
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
                print("inserted right: {}".format(data))
        else:
            self.data = data

    # Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()

# Use the insert method to add nodes
root = Node(27)
root.insert(14)
root.insert(35)
root.insert(31)
root.insert(10)
root.insert(19)

root.PrintTree()

# https://stackoverflow.com/questions/56863556/how-to-represent-binary-tree-into-an-array-using-python
# represent binarytree into an array
a =  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15]

def childNodes(i):
     return (2*i)+1, (2*i)+2

def traversed(a, i=0, d = 0):
    if i >= len(a):
        return 
    l, r =  childNodes(i)
    traversed(a, r, d = d+1)
    print("   "*d + str(a[i]))
    traversed(a, l, d = d+1)

traversed(a)



# Determine Traversal 
# https://www.geeksforgeeks.org/bfs-vs-dfs-binary-tree/
#    1
#  2   3
#4  5
# BST: 1 2 3 4 5
# DFT: 
#   Preorder: 1 2 4 5 3
#   Inorder: 4 2 5 1 3
#   Postorder: 4 5 2 3 1


