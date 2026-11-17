class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:

        if head is None or head.next is None:
            return head

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        temp = head

        while temp is not None and temp.next is not None:
            front = temp.next

     
            temp.next = front.next
            front.next = temp
            prev.next = front

        
            prev = temp
            temp = temp.next

        return dummy.next

     

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna