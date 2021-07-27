class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def isPalindrom(self, head):
        '''
        head: ListNode
        rtype:bool
        '''
        val_list = []
        curr = head
        while curr != None:
            val_list.append(curr.val)
            curr = curr.next
        print(val_list)
        return val_list[::-1] == val_list

        

s = Solution()
head1 = ListNode(1,ListNode(2))
assert s.isPalindrom(head1) == False

head2 = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
assert s.isPalindrom(head2) == True