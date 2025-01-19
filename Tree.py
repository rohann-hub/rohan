### Binary Tree Implementation:

class TreeNode:
    def __init__(self, value):
        self.value = value  
        self.children = []  

    def add_child(self, child_node):
        self.children.append(child_node) 

    def display_tree(self, level=0):
        print("  " * level + self.value) 
        for child in self.children:
            child.display_tree(level + 1)  

root = TreeNode('Root')     
child1 = TreeNode('Child1') 
child2 = TreeNode('Child2')
child3 = TreeNode('Child3')

root.add_child(child1)  
root.add_child(child2)  
child1.add_child(child3) 

root.display_tree()


#### Binary search Tree

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(node.right, value)

    def search(self, value):
        return self._search(self.root, value)

    def _search(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search(node.left, value)
        return self._search(node.right, value)

    def inorder(self):
        self._inorder(self.root)

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.value, end=" ")
            self._inorder(node.right)


if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)
    bst.insert(6)
    bst.insert(8)

    print("Inorder traversal:")
    bst.inorder()  

    print("\nSearch for 4:")
    result = bst.search(4)
    if result:
        print("Found:", result.value)  
    else:
        print("Not found")

