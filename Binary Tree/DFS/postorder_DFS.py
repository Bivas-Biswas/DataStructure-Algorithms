class Node:
    def __init__(self, data):
        self.key = data
        self.left = None
        self.right = None


def postorder(root):
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.key, end=" ")


if __name__ == "__main__":
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.right.left = Node(40)
    root.right.right = Node(50)

    postorder(root)
    #       10
    #     /    \
    #    20    30
    #         / \
    #       40  50
