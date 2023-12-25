# https://leetcode.com/problems/middle-of-the-linked-list/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    result = []
    while slow:
        result.append(slow.val)
        slow = slow.next

    return result

# Create linked list nodes
nodes1 = ListNode(1)
nodes1.next = ListNode(2)
nodes1.next.next = ListNode(3)
nodes1.next.next.next = ListNode(4)
nodes1.next.next.next.next = ListNode(5)

nodes2 = ListNode(1)
nodes2.next = ListNode(2)
nodes2.next.next = ListNode(3)
nodes2.next.next.next = ListNode(4)
nodes2.next.next.next.next = ListNode(5)
nodes2.next.next.next.next.next = ListNode(6)

# Call the function with linked list heads
result1 = middleNode(nodes1)  # Returns the values from the middle node: [3, 4, 5]
result2 = middleNode(nodes2)  # Returns the values from the middle node: [4, 5, 6]

print(result1)
print(result2)