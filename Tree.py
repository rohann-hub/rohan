### Tree Implementation:

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


#### 
