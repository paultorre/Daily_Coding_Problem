import heapq

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None


def link_k_linked_lists(lists):
    dummy = tail = ListNode(0)
    mh = []

    for i,h in enumerate(lists):
        heapq.heappush(mh,(h.val,i))
    while mh:
        print(mh)
        t = heapq.heappop(mh)
        tail.next = lists[t[1]]
        tail = tail.next
        lists[t[1]] = lists[t[1]].next
        if lists[t[1]]:
            heapq.heappush(mh,(lists[t[1]].val, t[1]))

    return dummy.next

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
# Call the func
ans = link_k_linked_lists([l1,l2, l3])

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

while ans:
    print(ans.val)
    ans = ans.next