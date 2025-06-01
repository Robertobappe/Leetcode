from typing import List  # Adicione esta linha no início do arquivo
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Brute force
        '''
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False
    Time complexity O(n^2)
    Space complexity O(1)
    '''

        # Best solution
        table = {}

        for i in nums:
            if i in table:
                return True
            table[i] = True
        
        return False
    # Time complexity O(n)
    # Space complexity O(n)

sol = Solution()
rel = sol.hasDuplicate([1,2,3,4])
print(rel)