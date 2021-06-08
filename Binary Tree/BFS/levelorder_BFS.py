class Node:
    def __init__(self, data):
        self.key = data
        self.left = None
        self.right = None


def levelorder(root):
    q = [root]
    while len(q):
        curr = q.pop(0)
        print(curr.key, end=" ")
        if curr.left:
            q.append(curr.left)
        if curr.right:
            q.append(curr.right)


if __name__ == "__main__":
    root = Node(3)
    root.left = Node(9)
    root.right = Node(20)
    root.right.left = Node(15)
    root.right.right = Node(7)
    #       10
    #     /    \
    #    20    30
    #   / \
    # 40  50
    levelorder(root)

