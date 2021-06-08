class Node:
    def __init__(self, data=0):
        self.key = data
        self.left = None
        self.right = None


def insertion(root, key):
    if not root:
        root = Node(key)
        return

    curr = root
    q = []
    q.append(curr)
    while len(q) != 0:
        curr = q[0]
        q.pop(0)

        if not curr.left:
            curr.left = Node(key)
            break
        else:
            q.append(curr.left)
        if not curr.right:
            curr.right = Node(key)
            break
        else:
            q.append(curr.right)


# levelorder traversal of a binary tree
def levelorder(root):
    q = []
    q.append(root)
    while len(q) != 0:
        curr = q.pop(0)
        print(curr.key, end=" ")
        if curr.left:
            q.append(curr.left)
        if curr.right:
            q.append(curr.right)


if __name__ == "__main__":
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.left.left = Node(40)
    root.right.right = Node(50)
    levelorder(root)

    #       10
    #     /    \
    #    20    30
    #   /        \
    # 40         50

    print()
    insertion(root, 12)
    levelorder(root)

    #       10
    #      /  \
    #    20    30
    #   / \      \
    # 40  12      50
