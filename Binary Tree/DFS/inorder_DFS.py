class Node:
    def __init__(self, data):
        self.key = data
        self.left = None
        self.right = None


def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.key, end=" ")
    inorder(root.right)


if __name__ == "__main__":
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.right.left = Node(40)
    root.right.right = Node(50)
    #       10
    #     /    \
    #    20    30
    #         / \
    #       40  50
    inorder(root)
