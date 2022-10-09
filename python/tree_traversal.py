class BinaryTree:

    def __init__(self, value):

        self.left = None
        self.right = None
        self.value = value

    # Insert Node
    def insert(self, value):
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = BinaryTree(value)
                else:
                    self.left.insert(value)
            elif value > self.value:
                if self.right is None:
                    self.right = BinaryTree(value)
                else:
                    self.right.insert(value)
        else:
            self.value = value

    # Print the Tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.value),
        if self.right:
            self.right.PrintTree()

    # Inorder traversal
    # Left -> Root -> Right
    def PrintInOrderTree(self):
        if self.left:
            self.left.PrintInOrderTree()
        
        print(self.value)
        
        if self.right:
            self.right.PrintInOrderTree()

    # Preorder traversal
    # Root -> Left -> Right
    def PrintPreOrderTree(self):
        print(self.value)
        if self.left:
            self.left.PrintPreOrderTree()

        if self.right:
            self.right.PrintPreOrderTree()

    # Postorder traversal
    # Left -> Right -> Root
    def PrintPostOrderTree(self):
        if self.left:
            self.left.PrintPostOrderTree()

        if self.right:
            self.right.PrintPostOrderTree()
        print(self.value)


root = BinaryTree(100)
root.insert(50)
root.insert(55)
root.insert(60)
root.insert(20)
root.insert(52)

print("Actual created tree: ")
root.PrintTree()

print("InOrder Traversal: ")
root.PrintInOrderTree()

print("Post Order Traversal: ")
root.PrintPostOrderTree()

print("Pre Order Traversal: ")
root.PrintPreOrderTree()
