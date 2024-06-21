# basically the movemnt is what matters of else revrse it 
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        cur=dummy
        
        for _ in range(n):
            head=head.next

        while head:
            head=head.next
            cur=cur.next
        cur.next=   cur.next.next
        return dummy.next  
