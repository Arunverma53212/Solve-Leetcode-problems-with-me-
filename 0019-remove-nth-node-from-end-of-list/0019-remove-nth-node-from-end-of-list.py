# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        count = 0
        temp = head

        while temp:
            count+=1
            temp = temp.next

        
        if count == n:
            new_node = head.next
            return new_node

        temp = head
        count-=n
        i = 1
        while i<count:
            i+=1
            temp = temp.next
            
        
        temp.next = temp.next.next
        return head







  

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna