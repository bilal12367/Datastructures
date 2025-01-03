from LinkedList import LL

l = LL()
arr = [1,2,3,4,5,6,7,8,9]
k = 2
head = l
for i in arr:
    l.val = i
    l.next = LL()
    l = l.next

def reverseLL(head):
    t = head
    prev = None
    while t is not None:
        temp = t.next
        t.next = prev
        prev = t
        t = temp
    return (prev,head)

def printLL(head):
    while head is not None:
        print(head.val, end = " --> ")
        head = head.next

h = temp = head
it = 1
st = []
while temp is not None:
    if it % k == 0:
        t = temp.next
        temp.next = None
        temp = t
        st.append((h,t))
        h = t
    if temp.next is None:
        st.append((h, temp))
        break
    it += 1
    temp = temp.next
temp = head
printLL(temp)
prev = None
for i in st[::-1]:
    (h,t) = reverseLL(i[0])
    print(h.val,", ", t.val)
    t.next = prev
    prev = h
    
temp = head = prev
printLL(temp)