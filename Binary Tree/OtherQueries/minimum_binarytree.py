class Node:
    def __init__(self, data):
        self.key = data
        self.left = None
        self.right = None


def getmin(root):
    if not root:
        return float('inf')  # return infinite
    return min(root.key, min(getmin(root.left), getmin(root.right)))


if __name__ == "__main__":
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.left.left = Node(40)
    root.left.right = Node(50)
    print(getmin(root))

    #        10
    #      /    \
    #     20    30
    #    / \
    # 40  50
