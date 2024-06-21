class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        second=slow.next
        slow.next=None
        prev=None
        while second:
            tmp=second.next
            second.next=prev
            prev=second
            second=tmp
        #merging two halves of list
        first=head
        second=prev   
        while second:
            tmp1,tmp2=first.next,second.next
            first.next=second
            second.next=tmp1
            first=tmp1
            second=tmp2
#so basically we are reversing the second half and merging those tow linked lists
