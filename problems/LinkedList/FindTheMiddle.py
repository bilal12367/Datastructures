
class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None

arr = [1,2,3,4,5,6,7,8]

head = Node(None)
start = head
prev = None
# Converting Array To LinkedList
for i in arr:
    start.data = i
    start.next = Node(None)
    prev = start
    start = start.next

start = head
slow = start
fast = start
while(fast.next != None and fast.next.next != None):
    slow = slow.next
    fast = fast.next.next
print("Middle of linkedlist is: ", slow.data, " i = ",i)