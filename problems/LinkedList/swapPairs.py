from LinkedListMod import LinkedList as LL, Node as N
def swapInPairs(head):
    start = head
    i = 1
    while start is not None:
        if i % 2 == 0:
            prev.val, start.val = start.val, prev.val
        prev = start
        start = start.next
        i += 1
    return head


head = LL([1,2,3,4]).getHead()
head = swapInPairs(head)
LL().printByHead(head)