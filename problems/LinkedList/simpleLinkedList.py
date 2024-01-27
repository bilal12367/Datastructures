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

del arr

# Traversing and Printing LinkedList
start = head
while(start.next):
    print(start.data)
    start = start.next

# Reversing LinkedList
start = head
new = start.next
prev = head
start.next = None
while(new.next):
    temp = new
    new = new.next
    temp.next = prev
    prev = temp
head = prev

# Checking LinkedList
print("==========================")
start = head
while(start != None):
    print(start.data)
    start = start.next

