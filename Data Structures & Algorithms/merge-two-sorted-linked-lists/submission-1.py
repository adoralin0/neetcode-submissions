# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1 and not list2:
            return None
        elif not list1:
            return list2
        elif not list2:
            return list1
        
        result = node = ListNode()
        while list1 and list2:
            next1 = list1.next
            next2 = list2.next
            val1 = list1.val
            val2 = list2.val
            if val1 <= val2:
                node.next = list1
                list1 = next1
            elif val2 <= val1:
                node.next = list2
                list2 = next2
            
            node = node.next
        node.next = list1 or list2
        return result.next
            


            
                

            
        