class Node:
    def __init__(self, data):
        self.key = data
        self.left = None
        self.right = None


def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.key, end=" ")
    inorder(root.right)


def deleteDeppest(root, d_node):
    q = []
    q.append(root)
    while len(q):
        temp = q.pop(0)

        if temp is d_node:
            temp = None
            return

        if temp.left:
            if temp.left is d_node:
                temp.left = None
                return
            else:
                q.append(temp.left)

        if temp.right:
            if temp.right is d_node:
                temp.right = None
                return
            else:
                q.append(temp.right)


def deletion(root, key):
    if root is None:
        return None
    if root.left is None and root.right is None:
        if root.key == key:
            return None
        else:
            return root
    key_node = None
    q = []
    q.append(root)
    while len(q):
        temp = q.pop(0)
        if temp.key == key:
            key_node = temp
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)
    if key_node:
        x = temp.key
        deleteDeppest(root, temp)
        key_node.data = x
    return root


if __name__ == "__main__":
    root = Node(10)
    root.left = Node(11)
    root.left.left = Node(7)
    root.left.right = Node(12)
    root.right = Node(9)
    root.right.left = Node(15)
    root.right.right = Node(8)
    print("The tree before the deletion:")
    inorder(root)

    #        10
    #      /    \
    #    11      9
    #   / \     / \
    #  7  12  15   8

    key = 11
    root = deletion(root, key)
    print()
    print("The tree after the deletion;")
    inorder(root)

    #        10
    #      /    \
    #     8      9
    #   / \     /
    #  7  12  15
