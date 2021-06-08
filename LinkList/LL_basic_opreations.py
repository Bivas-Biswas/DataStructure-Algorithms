class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkList:

    def __init__(self):
        self.head = None

    def append_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node

    def display(self):
        temp = self.head
        elem = []
        while temp != None:
            elem.append(temp.data)
            temp = temp.next
        print(elem)

    def lenght(self):
        temp = self.head
        total = 0
        while temp is not None:
            total += 1
            temp = temp.next
        print(total)

    def delete_node(self, key):
        temp = self.head

        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if temp is None:
            return print("Not Found 'o'")

        prev.next = temp.next

        temp = None


if __name__ == "__main__":
    llist = LinkList()
