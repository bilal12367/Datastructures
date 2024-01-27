class Node:
    def __init__(self,val = None) -> None:
        self.val = val
        self.next = None

    def printByHead(self,head):
        start = head
        while(head.next):
            print(start.val)
            start = start.next
    
    def printFromCurrent(self):
        start =  self
        while(start):
            print(start.val)
            start = start.next
    

def getYIntersection():
    arr1 = [ 1,2,6,5, 2,3, 4, 5, 6]
    arr2 = [8,7,3]
    dummy = Node()
    start = dummy
    j = 0
    intersect = None
    for i in arr1:
        j += 1
        newNode = Node(i)
        if j == 5:
            intersect = newNode
        start.next = newNode
        start = start.next
    head = dummy.next
    dummy = Node()
    print(intersect.val)
    start = dummy
    end = None
    for i in arr2:
        newNode = Node(i)
        start.next = newNode
        end = newNode
        start = start.next
    head2 = dummy.next
    end.next = intersect
    return head,head2
    
def getIntersectionNode(headA, headB):
    def getLength(head):
        start = head
        length = 0
        while(start):
            length += 1
            start = start.next
        return length
    
    lenA = getLength(headA)
    lenB = getLength(headB)

    startA = headA
    while(lenA > lenB):
        startA = startA.next
        lenA -= 1

    startB = headB
    while(lenB > lenA):
        startB = startB.next
        lenB -= 1
    
    
    while(startA != startB):
        startA = startA.next
        startB = startB.next
    
    return startA
    


if __name__ == '__main__':
    head1, head2 = getYIntersection()
    interNode = getIntersectionNode(head1, head2)
    print(interNode.val)
    
    
