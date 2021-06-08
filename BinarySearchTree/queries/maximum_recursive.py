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


def maximum(root):
    while root.right is not None:
        root = root.right
    return root.val


if __name__ == "__main__":
    r = node(50)
    r = insert(r, 30)
    r = insert(r, 20)
    r = insert(r, 3)
    r = insert(r, 60)
    r = insert(r, 30)
    inorder(r)
    print()
    print(maximum(r))
