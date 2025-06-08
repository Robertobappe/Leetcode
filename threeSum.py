from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        resp = []
        nums.sort()

        #We can fix one value
        for i,value in enumerate(nums):
            # We don't wanna use the same value used before
            #So we'll skip the current iteration of the loop
            if i > 0 and value == nums[i -1]:
                continue
            #TwoSum problem with two pointers
            l,r = i + 1, len(nums) - 1
            while l < r:
                threeSum = value + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    #We found a valid threeSum
                    resp.append([value, nums[l], nums[r]])
                    l += 1
                    # We don't wanna use the same value used before
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
        return resp
                    

def main():
    teste_cases = [
        [-1,0,1,2,-1,-4],
         [0,1,1],
         [0,0,0]
    ]

    sol = Solution()
    for numbers in teste_cases:
        result = sol.threeSum(numbers)
        print(result)

if __name__ == "__main__":
    main()