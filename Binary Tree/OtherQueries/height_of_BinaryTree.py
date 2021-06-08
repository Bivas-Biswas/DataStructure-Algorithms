class Node:
    def __init__(self, data):
        self.key = data
        self.left = None
        self.right = None


def height(root):
    if not root:
        return 0
    return max(height(root.left), height(root.right)) + 1


if __name__ == "__main__":
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.left.left = Node(40)
    root.left.right = Node(50)
    print(height(root))
    #        10
    #      /    \
    #     20    30
    #    / \
    # 40  50
