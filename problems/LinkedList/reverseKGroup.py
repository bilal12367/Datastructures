from LinkedListMod import Node, LinkedList

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
head = LinkedList(arr).getHead()
# LinkedList().printByHead(head)
# Reverse LinkedList


def reverseLinkedList(head, init=None) -> Node:
    start = head
    front = start
    prev = init
    while front is not None:
        temp = front.next
        front.next = prev
        prev = front
        front = temp

    return prev, head

# Not a complete solution
k = 3
i = 1
temp = None
start = head
begin = start
end = None
prev = start
remStart = None

while start is not None:
    if i % k == 0:
        temp = start.next
        start.next = None
        hd, prev = reverseLinkedList(begin)
        if i == 3:
            head = hd
        if hasattr(end, 'val'):
            end.next = hd
        end = prev
        begin = temp
        start = temp
        remStart = None
    else:
        if i % k == 1:
            remStart = start
        prev = start
        start = start.next
    i += 1

if hasattr(remStart, 'val'):
    hd = reverseLinkedList(remStart)
    print(LinkedList().printByHead(hd))

# LinkedList().printByHead(head)
