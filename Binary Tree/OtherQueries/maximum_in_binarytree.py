class Node:
    def __init__(self, data):
        self.key = data
        self.left = None
        self.right = None


def getmax(root):
    if root is None:
        return float('-inf')  # return -infinite
    return max(root.key, max(getmax(root.left), getmax(root.right)))


if __name__ == "__main__":
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.left.left = Node(40)
    root.left.right = Node(50)
    print(getmax(root))

    #        10
    #      /    \
    #     20    30
    #    / \
    # 40  50
