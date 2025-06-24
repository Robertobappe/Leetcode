from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        resp = []

        # We fix one 
        for i in range(len(nums) - 1):
            # Once the list is sorted, we don't want the new valeu has
            #the same previous value
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # We fix two
            for j in range(i+1, len(nums)):
                # Once the list is sorted, we don't want the new valeu has
                #the same previous value
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                
                # Two pointers problem
                left, right = j+1, len(nums) - 1                
                while left < right:
                    if nums[i] + nums[j] + nums[left] + nums[right] > target:
                        right -= 1
                    elif nums[i] + nums[j] + nums[left] + nums[right] < target:
                        left += 1
                    else:
                        resp.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        # Once the list is sorted, we don't want the new valeu has
                        #the same previous value
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
        return resp

# Try to undertand the recursion solution!!

def main():
    testes_cases = [
        ([1,0,-1,0,-2,2], 0),
        ([2,2,2,2,2], 8),
        ([-2,-1,-1,1,1,2,2], 0)
    ]

    sol = Solution()
    for numbers, target in testes_cases:
        result = sol.fourSum(numbers, target)
        print(result)

if __name__ == "__main__":
    main()