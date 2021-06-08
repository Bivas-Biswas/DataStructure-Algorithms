class node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


def inorder(root):
    if not root:
        return None
    inorder(root.left)
    print(root.val, end=" ")
    inorder(root.right)


def insert(root, key):
    if not root:
        return node(key)
    else:
        if root == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root


def minimum(root):
    while root.left is not None:
        root = root.left
    return root


def inOrderSuccessor(root, succ, key):
    if root is None:
        return None

    if root.val == key:
        if root.right:
            return minimum(root.right)

    elif root.val > key:
        succ = root
        return inOrderSuccessor(root.left, succ, key)
    else:
        return inOrderSuccessor(root.right, succ, key)

    return succ


if __name__ == "__main__":
    keys = [15, 10, 20, 8, 12, 16, 25]

    #            15
    #          /    \
    #         /      \
    #        10       20
    #       / \      /  \
    #      /   \    /    \
    #     8    12  16    25

    root = None
    for key in keys:
        root = insert(root, key)
    succ = 0
    prec = inOrderSuccessor(root, succ, 12)
    print(prec.val)
