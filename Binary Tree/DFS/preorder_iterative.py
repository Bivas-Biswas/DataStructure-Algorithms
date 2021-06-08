class Node:
    def __init__(self, data):
        self.key = data
        self.left = None
        self.right = None


def iterative_preorder(root):
    if root is None:
        return root
    st = []
    st.append(root)
    while len(st) != 0:
        curr = st[-1]
        print(curr.key, end=" ")
        st.pop()
        if curr.right is not None:
            st.append(curr.right)
        if curr.left is not None:
            st.append(curr.left)


if __name__ == "__main__":
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.left.left = Node(40)
    root.left.right = Node(50)
    root.right.left = Node(60)

    iterative_preorder(root)
    #        10
    #      /    \
    #     20    30
    #    / \   /
    # 40  50  60
