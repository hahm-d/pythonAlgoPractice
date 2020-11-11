# Definition for singly-linked list.
# 1290. Convert Binary Number in a Linked List to Integer
# 876. Middle of the Linked List
# 83. Remove Duplicates from Sorted List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# create a sample singly-linked list
nodeA = ListNode()
nodeB = ListNode()
nodeC = ListNode()
nodeA.val = 0
nodeB.val = 1
nodeC.val = 1
nodeA.next = nodeB
nodeB.next = nodeC

listA = ListNode()
listA1 = ListNode()
listA2 = ListNode()
listA.val = 1
listA1.val = 2 
listA2.val = 3
listA.next = listA1
listA1.next = listA2

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        num = head.val
        while head.next:
            num = num * 2 + head.next.val
            print(num)
            head = head.next
        return num
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            print(fast.val)
            slow = slow.next
            fast = fast.next.next
        return slow
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None: #python uses None not Null for empty 
            return head
        node = head
        while node:
            while node.next and node.next.val == node.val:
                node.next = node.next.next
            node= node.next
        return head
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        curr = head
        while l1 and l2:
            print(l1.val, l2.val)
            if l1 and l2 and l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            elif l1 and l2 and l2.val <= l1.val:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2
        return head.next  


solution = Solution()
#print(Solution.getDecimalValue(0,nodeA))
#print(Solution.middleNode(0,listA))
#print(Solution.deleteDuplicates(0,nodeA))
#Solution.mergeTwoLists(0, listA, nodeA)