# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        arr1=[]
        arr2=[]
        
        rl1,curr=None,l1 
        while curr: 
            temp=curr.next 
            curr.next=rl1 
            rl1=curr 
            curr=temp
        curr=rl1

        while curr:
            arr1.append(curr.val)
            curr=curr.next
        arr1 = int(''.join(map(str, arr1)))
        
        rl2,curr=None,l2 
        while curr: 
            temp=curr.next 
            curr.next=rl2 
            rl2=curr 
            curr=temp
        
        curr=rl2
        while curr:
            arr2.append(curr.val)
            curr=curr.next
        arr2 = int(''.join(map(str, arr2)))

        total=str(arr1+arr2)

        dummy=ListNode(0)
        tail=dummy
        for i in reversed(total):
            tail.next=ListNode(int(i))
            tail=tail.next
        return dummy.next

        
        
        