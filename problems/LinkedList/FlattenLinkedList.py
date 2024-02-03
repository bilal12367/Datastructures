class Node:
    def __init__(self, val=None, next=None, down=None) -> None:
        self.val = val
        self.next = next
        self.down = down

    def addNodesToDown(self, count):
        dummy = Node()
        dummy.down = self.down
        start = dummy
        for i in range(1, count+1):
            newNode = Node(i)
            start.down = newNode
            start = start.down
        self.down = dummy.down
        return self

    def printNodesToDown(self):
        start = self.down
        str1 = ""
        print("============")
        while start is not None:
            str1 += str(start.val) + ' ==> '
            start = start.down
        print(str1)
        print("============")


head = Node(1, Node(2, Node(3, Node(4, Node(5))).addNodesToDown(2)
                    ).addNodesToDown(1)).addNodesToDown(4)
start = head
while start is not None:
    print(start.val)
    start.printNodesToDown()
    start = start.next
start = head
while start is not None:
    current = start
    next = start.next if start.next is not None else None
    if current.down is not None:
        start1 = start.down
        while start1 is not None:
            start.next = start1
            start = start.next
            start1 = start1.down
        start.down = None
        start.next = next
    else:
        start.down = None
        start = start.next

start = head
while start is not None:
    print(start.val)
    start = start.next
