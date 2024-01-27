from LinkedListMod import Node, LinkedList

def checkPalindrome(head):
    if head == None or head.next == None:
        return True
    dummy = Node(0)
    dummy.next = head
    tortoise = dummy
    hare = head
    stack = []
    # Move hare twice as fast as tortoise
    while hare is not None and hare.next is not None:
        tortoise = tortoise.next
        stack.append(tortoise.val)
        hare = hare.next.next
    print(stack)
    test = stack.pop()
    stack.append(test)
    flag = True
    start = None
    if tortoise.next.val == test:
        start = tortoise.next
    else:
        start = tortoise
    while (start.next):
        if len(stack) == 0:
            flag = False
            break
        temp = stack.pop()
        if (start.val != temp):
            flag = False
        start = start.next

    if flag and len(stack) == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    list = LinkedList([])
    head = list.getHead()
    
