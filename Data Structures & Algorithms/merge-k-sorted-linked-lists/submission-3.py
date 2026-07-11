# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists:
            return None

        def merge(l1, l2):

            dummy = ListNode()
            tail = dummy

            while l1 and l2:
                if l1.val < l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                
                tail = tail.next
            
            tail.next = l1 if l1 else l2

            return dummy.next

        while len(lists) > 1:

            merged = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]

                if i+1 < len(lists):
                    l2 = lists[i+1]
                else:
                    l2 = None

                merged.append(merge(l1,l2))

            lists = merged

        return merged[0]

            




        # if not lists:
        #     return None

        # def mergeList(l1,l2):
        #     dummy = ListNode()
        #     tail = dummy

        #     while l1 and l2:
        #         if l1.val < l2.val:
        #             tail.next = l1
        #             l1 = l1.next
        #         else:
        #             tail.next = l2
        #             l2 = l2.next

        #         tail = tail.next
            
        #     tail.next = l1 if l1 else l2
        #     return dummy.next

        # while len(lists)>1:
        #     merged = []
        #     for i in range(0,len(lists),2):
        #         l1 = lists[i]

        #         if i+1 < len(lists):
        #             l2 = lists[i+1]
        #         else:
        #             l2 = None

        #         merged.append(mergeList(l1,l2))

        #     lists = merged

        # print(len(lists))
        # return lists[0]













        # if not lists:
        #     return None

        # def merge_2list(l1,l2):
        #     dummy = ListNode()
        #     tail = dummy

        #     while l1 and l2:
        #         if l1.val < l2.val:
        #             tail.next = l1
        #             l1 =l1.next
        #         else:
        #             tail.next = l2
        #             l2 = l2.next

        #         tail = tail.next
            
        #     tail.next = l1 if l1 else l2

        #     return dummy.next

        # while len(lists) > 1:
        #     merged = []
        #     for i in range(0, len(lists), 2):

        #         l1 = lists[i]

        #         if i+1 < len(lists):
        #             l2 = lists[i+1]
        #         else:
        #             l2 = None

        #         merged.append(merge_2list(l1,l2))

        #     lists = merged

        # return lists[0]