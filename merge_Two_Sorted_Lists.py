# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



#https://leetcode.ca/2015-12-21-21-Merge-Two-Sorted-Lists/
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # We can also use iteration to implement the merging of two sorted linked lists.
        # First, we define a dummy head node "dummy" 
        dummy = ListNode()
        current = dummy
        #

        while list1 or list2:
            v1 = list1.val if list1 else float('inf')
            v2 = list2.val if list2 else float('inf')

            #If the value of the head node of l1 is less than or equal to the value of the head node of l2,
            if  v1 < v2:
                current.next = list1
                list1 = list1.next
                # we recursively call the function mergeTwoLists(l1.next, l2), and connect the head node of l1
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        return dummy.next
        # with the returned linked list head node, and return the head node of l1.
