
#  Write a python program to inplement  the 2-3  Tree 

class Node: 
    def __init__(self):
        self.keys = []
        self.children = [] 

class TwoThreeTree: 
    def __init__(self):
        self.root = Node()

    def insert(self, key):
        root = self.root

        if len(root.keys) == 2:
            new_root = Node()
            new_root.children.append(root)
            self.split_child(new_root, 0)
            self.root = new_root

        self.insert_non_full(self.root, key)

    def insert_non_full(self, node, key):
        if not node.children:
            node.keys.append(key)
            node.keys.sort()
        else:
            i = len(node.keys) - 1
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1

            if len(node.children[i].keys) == 2:
                self.split_child(node, i)
                if key > node.keys[i]:
                    i += 1

            self.insert_non_full(node.children[i], key)

    def split_child(self, parent, i):
        node = parent.children[i]
        new_node = Node()

        mid = node.keys[1]

        left_keys = [node.keys[0]]
        right_keys = []

        if len(node.keys) == 3:
            right_keys = [node.keys[2]]

        new_node.keys = right_keys
        node.keys = left_keys

        if node.children:
            new_node.children = node.children[2:]
            node.children = node.children[:2]

        parent.keys.insert(i, mid)
        parent.children.insert(i + 1, new_node)

    def inorder(self, node):
        if node:
            if len(node.keys) == 1:
                if node.children:
                    self.inorder(node.children[0])
                print(node.keys[0], end=" ")
                if node.children:
                    self.inorder(node.children[1])
            elif len(node.keys) == 2:
                if node.children:
                    self.inorder(node.children[0])
                print(node.keys[0], end=" ")
                if node.children:
                    self.inorder(node.children[1])
                print(node.keys[1], end=" ")
                if node.children:
                    self.inorder(node.children[2])

# Test
tree = TwoThreeTree()
data = [10, 20, 5, 6, 12, 30, 7, 17]

for x in data:
    tree.insert(x)

print("Inorder Traversal:")
tree.inorder(tree.root)