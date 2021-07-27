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
        max_ = 10**4
        idx = 0
        while idx <= max_:
            if not head:
                return False
            head = head.next 
            idx += 1 
        return True