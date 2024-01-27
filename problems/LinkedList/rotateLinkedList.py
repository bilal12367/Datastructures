from LinkedListMod import LinkedList as LL, Node


def rotateLL(head, k):
    if k == 0:
        return head
    prev = front = head
    for i in range(k):
        if front.next is None:
            if i == k - 1:
                return head
            front = head
        else:
            front = front.next

    while front.next is not None:
        front = front.next
        prev = prev.next
    tmp = prev.next
    prev.next = None
    front.next = head
    head = tmp
    return head


for k in range(1, 20):
    print("==========================")
    print("For k = ", k)
    head = LL([1, 2, 3, 4, 5, 6, 7, 8, 9]).getHead()
    head1 = rotateLL(head, k)
    LL().printByHead(head1)
    print("==========================")
