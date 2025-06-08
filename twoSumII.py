from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #Solution usuing space complexity of O(n)
        '''
        mapNum = {}
        for index,value in enumerate(numbers):
            complement = target - value
            if complement in mapNum:
                return [mapNum[complement] + 1, index + 1]
            mapNum[value] = index'''
        
        #Solution with space complexity of O(1)
        l,r = 0, len(numbers) - 1
        
        while l < r:
            sumPointers = numbers[l] + numbers[r]
            if sumPointers > target:
                r -= 1
            elif sumPointers < target:
                l += 1
            else:
                return [l+1,r+1]

def main():
    test_cases = [
        ([2,7,11,15], 9),
        ([2,3,4], 6),
        ([-1,0], -1)
    ]

    solution = Solution()
    for numbers, target in test_cases:
        result = solution.twoSum(numbers,target)
        print(result)
    
if __name__ == "__main__":
    main()

