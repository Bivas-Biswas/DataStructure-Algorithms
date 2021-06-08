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
    temp = node(key)
    parent = None
    curr = root

    # this loop use for reach the right position and store the node
    # in parent

    while curr is not None:
        parent = curr
        if curr.val > key:
            curr = curr.left
        elif curr.val < key:
            curr = curr.right
        else:
            return root

    # after get the parent ,now join the child in temp(key node)

    if parent is None:  # if is their is no root
        return temp
    if parent.val > key:
        parent.left = temp
    else:
        parent.right = temp
    return root


if __name__ == "__main__":
    r = node(50)
    r = insert(r, 30)
    r = insert(r, 20)
    r = insert(r, 3)
    r = insert(r, 60)
    r = insert(r, 30)
    inorder(r)
