# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        newnode = ListNode(0)
        curr = newnode
        temp1 = list1
        temp2 = list2

        while temp1 != None and temp2 != None:
            if temp1.val < temp2.val:
                curr.next = ListNode(temp1.val)
                curr = curr.next
                temp1 = temp1.next

            else:
                curr.next = ListNode(temp2.val)
                curr = curr.next
                temp2 = temp2.next
            
        
        if temp1 != None:
            while temp1 != None:
                curr.next = ListNode(temp1.val)
                curr = curr.next
                temp1 = temp1.next

        if temp2 != None:
            while temp2 != None:
                curr.next = ListNode(temp2.val)
                curr = curr.next
                temp2 = temp2.next

        return newnode.next
        
    
        

                

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna