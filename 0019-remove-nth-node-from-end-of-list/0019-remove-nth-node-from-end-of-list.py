# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev,curr=None,head
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        curr=prev
        if n==1:
            prev=prev.next
        else:
            for i in range(n-2):
                curr=curr.next
            curr.next=curr.next.next
           
        curr=prev
        prev=None
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        return prev

        