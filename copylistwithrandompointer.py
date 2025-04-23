# A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

# Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

# For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

# Return the head of the copied linked list.

# The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
# Your code will only be given the head of the original linked list.

class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
    

class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return None
        
        d1 = {}  # Dictionary to store mapping of original -> copied nodes
        
        # Step 1: Create deep copy of nodes (without random pointers)
        currnode = head
        dummy = Node(0)  # Dummy node to track new list
        new_curr = dummy
        
        while currnode:
            new_node = Node(currnode.val)  # Create new node
            d1[currnode] = new_node        # Map original -> copied
            new_curr.next = new_node       # Append to new list
            new_curr = new_curr.next
            currnode = currnode.next
        
        # Step 2: Assign random pointers
        currnode = head
        new_curr = dummy.next  # Start from copied list head

        while currnode:
            if currnode.random:
                new_curr.random = d1[currnode.random]  # Set correct random pointer
            currnode = currnode.next
            new_curr = new_curr.next
        
        return dummy.next  # Return the copied list's head