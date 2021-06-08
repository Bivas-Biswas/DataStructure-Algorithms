class Node:
    def __init__(self, data):
        self.key = data
        self.left = None
        self.right = None


def iterative_inorder(root):
    curr = root
    st = []
    while curr is not None or len(st) != 0:
        while curr is not None:
            st.append(curr)
            curr = curr.left
        curr = st.pop()
        print(curr.key, end=" ")
        curr = curr.right


if __name__ == "__main__":
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.left.left = Node(40)
    root.left.right = Node(50)
    iterative_inorder(root)
    #       10
    #     /    \
    #    20    30
    #   / \
    # 40  50
