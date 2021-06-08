class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linklist:
    def __init__(self):
        self.head = None

    def printList(self):
        elem = []
        temp = self.head
        while temp:
            elem.append(temp.data)
            temp = temp.next
        print(elem)

    def append_node(self, data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node


def mergeLists(headA, headB):

    dummyNode = node(0)
    tail = dummyNode
    while True:
        if headA is None:
            tail.next = headB
            break

        if headB is None:
            tail.next = headA
            break

        if headA.data <= headB.data:
            tail.next = headA
            headA = headA.next
        else:
            tail.next = headB
            headB = headB.next
        tail = tail.next

    return dummyNode.next


if __name__ == "__main__":
    llist1 = linklist()
    llist1.append_node(3)
    llist1.append_node(4)
    llist1.append_node(5)
    llist1.append_node(6)
    print("list A : ")
    llist1.printList()

    llist2 = linklist()
    llist2.append_node(2)
    llist2.append_node(3)
    llist2.append_node(10)
    print("list B : ")
    llist2.printList()

    print("Merge List : ")
    llist1.head = mergeLists(llist1.head, llist2.head)
    llist1.printList()
