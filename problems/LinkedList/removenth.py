import math


class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None


class LinkedList:

    def __init__(self, arr) -> None:
        self.head = Node(None)
        start = self.head
        for i in arr:
            start.val = i
            start.next = Node(None)
            start = start.next

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
        while start.next is not None:
            print(start.val)
            start = start.next


def deleteFromNthLast(head, n):
    dummy = Node(0)
    dummy.next = head
    slow = dummy
    fast = head

    for _ in range(n+1):
        fast = fast.next

    while fast is not None:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next
    return dummy.next


def addTwoLinkedList(l1, l2) -> Node:
    dummy = Node(0)
    temp = dummy
    carry = 0
    while (l1.val != None or l2.val != None) or carry:
        carry = 0
        sum = 0
        if l1.val != None:
            sum += l1.val
            l1 = l1.next
        if l2.val != None:
            sum += l2.val
            l2 = l2.next
        sum += carry
        carry = sum // 10
        node = Node(sum % 10)
        temp.next = node
        temp = temp.next
        print(temp.val)
    
    return dummy.next
    # carry = 0
    # sum = 0
    # dummy = Node(0)
    # start = dummy
    # while(l1 != None or l2  != None or carry):
    #     if l1 != None:
    #         sum += l1.val
    #         l1 = l1.next
    #     if l2 != None:
    #         sum += l2.val
    #         l2 = l2.next

    #     start.next = Node(sum%10)
    #     carry = math.floor(sum//10)
    #     start = start.next

    # return dummy.next


if __name__ == '__main__':
    # arr = [1, 2, 3, 4, 5, 6]
    # list.insertAt(4,12)
    # list.printByHead(head)
    # for i in range(1,7):
    #     print("=================== for i = ",i)
    #     list = LinkedList(arr)
    #     head = list.getHead()
    #     head = deleteFromNthLast(head, i)
    #     list.printByHead(head)
    # list.printByHead(head)

    list1 = LinkedList([2, 4, 3])
    list2 = LinkedList([5, 6, 4])
    head = addTwoLinkedList(list1.head, list2.head)
    list1.printByHead(head)
