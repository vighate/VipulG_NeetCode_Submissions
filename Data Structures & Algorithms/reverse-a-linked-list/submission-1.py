# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev
        
        # Traverse

        # curr = head
        # while curr:
        #     print(curr.val)
        #     curr = curr.next

        # Add node to start

        # newNode = ListNode(100)
        # newNode.next = head
        # head = newNode

        # curr = head
        # while curr:
        #     print(curr.val)
        #     curr = curr.next

        # Add node to end

        # newNode = ListNode(1000)
        # curr = head

        # while curr.next:
        #     curr = curr.next

        # curr.next = newNode

        # curr = head

        # while curr:
        #     print(curr.val)
        #     curr = curr.next

        # Insert after a Node

        # curr = head
        # newNode = ListNode(10000)

        # while curr.next and curr.val != 1:
        #     curr = curr.next 

        # newNode.next = curr.next
        # curr.next = newNode

        # curr = head

        # while curr:
        #     print(curr.val)
        #     curr = curr.next

        # Delete first Node
        
        # head = head.next
        # curr = head
        # while curr:
        #     print(curr.val)
        #     curr = curr.next
        
        # Delete last Node

        # curr = head
        # while curr.next.next:
        #     curr = curr.next
        # curr.next = None
        # curr = head
        # while curr:
        #     print(curr.val)
        #     curr = curr.next

        # Delete a node by Value

        # dummy = ListNode(0)
        # dummy.next = head
        # curr = head
        # prev = dummy

        # while curr:
        #     if curr.val == 2:
        #         prev.next = curr.next
        #         break
        #     prev = curr
        #     curr = curr.next

        # head = dummy.next
        # curr = head
        # while curr:
        #     print(curr.val)
        #     curr = curr.next

        # Search
        # curr = head
        # while curr:
        #     if curr.val == 2:
        #         print(True)
        #         break
        #     curr = curr.next

        # Count nodes
        # count = 0
        # curr = head
        # while curr:
        #     count +=1
        #     curr = curr.next
        # print(count)

        # Reverse Linklist

        # prev = None
        # curr = head

        # while curr:
        #     nxt = curr.next
        #     curr.next = prev

        #     prev = curr
        #     curr = nxt

        # head = prev
        # while head:
        #     print(head.val)
        #     head = head.next

        # Find Middle Node

        # slow = head
        # fast = head

        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        # print(slow.val)

        # Detect Cycle

        # slow = head
        # fast = head

        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next

        #     if slow == fast:
        #         print(True)

        # Merge two LL
        # dummy = ListNode()
        # tail = dummy

        # while l1 and l2:
        #     if l1.val < l2.val:
        #         tail.next = l1
        #         l1 = l1.next
        #     else:
        #         tail.next = l2
        #         l2 = l2.next

        #     tail = tail.next

        # tail.next = l1 if l1 else l2
        # head = dummy.next

