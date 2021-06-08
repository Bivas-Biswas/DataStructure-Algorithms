class node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


def inorder(root):
    if not root:
        return 0
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


def maximum(root):
    while root.right is not None:
        root = root.right
    return root


def minimum(root):
    while root.left is not None:
        root = root.left
    return root


def delete(root, key):
    if root is None:
        return root

    if key < root.val:
        root.left = delete(root.left, key)

    elif key > root.val:
        root.right = delete(root.right, key)

    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # if deleted node hava two child
        # use successor (below)

        # successor = minimum(root.right)
        # root.val = successor.val
        #
        # root.right = delete(root.right, successor.val)

        # or predecessor (below)

        predecessor = maximum(root.left)
        root.val = predecessor.val

        root.left = delete(root.left, predecessor.val)

    return root


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
    print(inorder(root))
    delete(root, 20)
    print()
    print(inorder(root))
