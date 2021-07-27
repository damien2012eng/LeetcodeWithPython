class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev_, curr = None, head
        while curr: 
            next_ = curr.next
            curr.next = prev_
            prev_ = curr
            curr = next_ 
        return prev_
    