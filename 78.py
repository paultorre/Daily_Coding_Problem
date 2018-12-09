from random import randint
import heapq

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

l1 = ListNode(0)
l2 = ListNode(0)
l3 = ListNode(0)

t = l1
for i in range(0,20,2):
    n = ListNode(i)
    t.next = n
    t = t.next

t = l2
for i in range(0,20,3):
    n = ListNode(i)
    t.next = n
    t = t.next

t = l3
for i in range(0,20,4):
    n = ListNode(i)
    t.next = n
    t = t.next

# the lists
k_lists = [l1,l2,l3]

print('LIST 1: ', end=' ')
while l1:
    print(l1.val,'-> ',end='') if l1.next is not None else print(l1.val)
    l1 = l1.next

print('LIST 2: ', end=' ')
while l2:
    print(l2.val,'-> ',end='') if l2.next is not None else print(l2.val)
    l2 = l2.next

print('LIST 3: ', end=' ')
while l3:
    print(l3.val,'-> ',end='') if l3.next is not None else print(l3.val)
    l3 = l3.next


#   Make a list of all the pointers to a list.  
#   While there are still nodes to merge, push all values into a heap as a tuple also containing info about which list they are from.
#   Pop the minium, then link to final answer.  
#
#   Time - O(N)  Linear on the order of the length of the lists.  Every node in every list must be touched once
#   Space - O(N)  Same as time.
head = tail = ListNode(0)

while any(k_lists):

    mheap = []
    for i in range(len(k_lists)):
        heapq.heappush(mheap,(k_lists[i].val,i)) if k_lists[i] else None

    n,i = heapq.heappop(mheap)
    tail.next = ListNode(n)
    
    k_lists[i] = k_lists[i].next
            

    tail = tail.next
    
print('MERGED: ', end=' ')
ans = head.next
while ans:
    print(ans.val,'-> ',end='') if ans.next is not None else print(ans.val)
    ans = ans.next





