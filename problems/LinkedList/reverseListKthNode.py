from LinkedListMod import LinkedList as LL, Node


def reverseLL(head):
    start = head
    prev = None
    while start is not None:
        temp = start.next
        start.next = prev
        prev = start
        start = temp

    return prev, head


def reverseListByKGroups(head, k):
    start = head
    i = 1
    begin = start
    end = None
    head1 = None
    while start is not None:
        if i % k == 0:
            temp = None
            if start.next is not None:
                temp = start.next
            start.next = None
            hd, end1 = reverseLL(begin)
            if head1 is None:
                head1 = hd
            if end is not None:
                end.next = hd
            end = end1
            end1.next = temp
            start = temp
            begin = temp
        else:
            start = start.next
        i += 1

    return head1


head = LL([1, 2 ]).getHead()

head = reverseListByKGroups(head, 2)
LL().printByHead(head)
