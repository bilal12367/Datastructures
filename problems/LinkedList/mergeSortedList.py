from LinkedListMod import LinkedList as LL, Node as ListNode


def merge_2_sortedList(head1, head2):
    dummy = N()
    start = dummy
    while head1 is not None or head2 is not None:
        if head1.val < head2.val:
            start.val = head1.val
            head1 = head1.next
        elif head1.val > head2.val:
            start.val = head2.val
            head2 = head2.next
        else:
            start.val = head1.val
            start.next = N(head2.val)
            head1 = head1.next
            head2 = head2.next


def hasNext(heads, cont=False):
    for i in heads:
        cont = cont or (True if i.next is not None else False)
    return cont


def mergeSortedList(heads):
    res = []
    while (True):
        arr = []
        flag = 0
        for i in range(len(heads)):
            if heads[i] is not None:
                arr += [heads[i].val]
                heads[i] = heads[i].next
                flag = 1
        res += arr
        if flag == 0:
            break
    res.sort()
    dummy = ListNode(0)
    start = dummy
    for i in res:
        start.next = ListNode(i)
        start = start.next

    return dummy.next



res = mergeSortedList([LL([1, 4, 5]).getHead(), LL(
    [1, 3, 4]).getHead(), LL([2, 6]).getHead()])

res.sort()
dummy = N(0)
start = dummy
for i in res:
    start.next = N(i)
    start = start.next

head = dummy.next
LL().printByHead(head)
