class Node:
    def __init__(self, data):
        self.key = data
        self.left = None
        self.right = None


def iterative_preorder(root):
    st = []

    # st.append(root) # for less implemention

    curr = root
    while len(st) != 0 or curr is not None:
        while curr is not None:
            print(curr.key, end=" ")
            if curr.right is not None:
                st.append(curr.right)
            curr = curr.left

        # curr = st.pop()  # for less implemention

        if len(st) != 0:
            curr = st[-1]
            st.pop()


if __name__ == "__main__":
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.left.left = Node(40)
    root.left.right = Node(50)
    root.left.right.right = Node(60)
    iterative_preorder(root)

    #        10
    #      /    \
    #     20    30
    #    / \
    # 40  50
    #      \
    #       60
