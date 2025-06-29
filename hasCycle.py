# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Time  complexity O(n)
        # Space complexity O(n)
        '''
        seen_nodes  = set()
        current = head
        iteration = True
        while iteration:
            iteration = False
            if current is None:
                return False
            elif current in seen_nodes :
                return True
            else:
                # Armazenando o endereço de memória de cada node e não o valor
                seen_nodes.add(current)
                if current.next == None:
                    return False
                iteration = True
                current = current.next'''
        
        # Floyd's Tortoise and Hare
        # Time complexity O(n)
        # Space complexity O(1)
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        
        return False
        