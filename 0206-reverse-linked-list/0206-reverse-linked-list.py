class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        temp = head
        prev = None
        while temp != None:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        return prev


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna