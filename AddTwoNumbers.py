"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x #value of node
        self.next = None #next node 

class LinkedList(object):
    def __init__(self):
        self.head = None
 
    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = ListNode(new_data)
        new_node.next = self.head
        self.head = new_node
        
    def addTwoNumbers(self, l1, l2):
        #dummy head of returning List
        dummy = ListNode(0)
        current = dummy
        p, q = l1, l2
        carry = 0
        val = carry #val is now the head of l1 l2
        while l1 or l2:
            if p:
                x = p.val
            else:
                x = 0 
            if q:
                y = q.val
            else:
                y = 0 
            sum = x + y + carry
            carry = sum/10
            current.next = ListNode(sum%10)
            current = current.next
            if p:
                p = p.next
            if q:
                q = q.next
        if carry > 0:
            current.next = ListNode(carry)
        
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.val)
            temp = temp.next
            
l1 = LinkedList()
l1.push(3)
l1.push(4)
l1.push(2)
print("first list", l1.printList())

l2 = LinkedList()
l2.push(4)
l2.push(6)
l2.push(5)
print("\nsecond list", l2.printList())

solution = LinkedList()
solution.addTwoNumbers(l1.head, l2.head)
print("\n Solution list", solution.printList)
