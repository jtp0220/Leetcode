class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

    @staticmethod
    def buildLL(arr):
        if not arr:
            return None    
        dum = ListNode()
        cur = dum
        for val in arr:
            cur.next = ListNode(val)
            cur = cur.next
        return dum.next
    
    @staticmethod
    def LLtoArray(head):
        result = []
        cur = head
        while cur:
            result.append(cur.val)
            cur = cur.next
        return result