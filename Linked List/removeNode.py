class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self,head, n):
        '''
        node: ListNode
        rtype: do not return anything. Modify node in-place
        '''
        dummy = ListNode(0)
        dummy.next = head
        fast = dummy
        slow = dummy
        i = 0
        while i <= n: 
            fast = fast.next
            i += 1
        while fast:
            fast = fast.next
            slow =slow.next
        slow.next = slow.next.next
        return dummy.next

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
s = Solution()
print(s.removeNthFromEnd(head, 2))
