# 147
#
def insertionSortList(head):
    if not head or not head.next:
        return head
    cur = head.next
    head.next = None
    while cur:
        this = cur
        cur = cur.next
        this.next = None
        check = head
        pre = None
        while check:
            if check.val > this.val:
                break
            pre = check
            check = check.next
        if pre is not None:
            pre.next = this
            this.next = check
        else:
            this.next = head
            head = this
    return head