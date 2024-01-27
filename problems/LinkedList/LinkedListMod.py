
class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None


class LinkedList:

    def __init__(self, arr = []) -> None:
        dummy = Node(None)
        start = dummy
        for i in arr:
            start.next = Node(i)
            start = start.next
        self.head = dummy.next

    def printList(self):
        start = self.head
        while start.next is not None:
            print(start.val)
            start = start.next

    def getHead(self) -> Node:
        return self.head

    def insertAt(self, n, val):
        start = self.head
        prev = start
        newNode = Node(val)
        i = 0
        if n == 0:
            newNode.next = start
            self.head = newNode
        else:
            while i < n:
                prev = start
                start = start.next
                i += 1
            temp = prev.next
            prev.next = newNode
            newNode.next = temp

    def deleteAt(self, n):
        start = self.head
        prev = start
        if n == 0:
            self.head = start.next
        else:
            i = 0
            while (i < n):
                prev = start
                start = start.next
                i += 1
            prev.next = prev.next.next

    def printByHead(self, newHead):
        start = newHead
        while start is not None:
            print(start.val)
            start = start.next
