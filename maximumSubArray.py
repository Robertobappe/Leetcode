# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # DFS
        # Time complexity O(n)
        # Space complexity O(n)
        
        if root is None:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
        #BFS
        '''
        from collections import deque
        level = 0

        q = deque([root])

        while q:
            for i in range(len(q)):
                #Pega o próximo nó da fila (da esquerda para a direita) FIFO
                node = q.popleft() 

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1

        return level'''
                