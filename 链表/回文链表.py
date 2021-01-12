# 234
# author official
# 将链表转化成列表

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def isPalindrome(self, head: ListNode):
        vals = []
        cur = head
        while cur is not None:
            vals.append(cur.val)
            cur = cur.next
        return vals == vals[::-1]




ss = Solution()
