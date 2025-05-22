#Brute force
def TwoSum1(nums,target):
    for i in range(len(nums) - 1):
        for j in range(i+1,len(nums)):
            if(nums[i] + nums[j] == target):
                return [i,j]
    return None
            

#Better solution
def TwoSum2(nums,target):
    map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in map:
            return [map[complement],i] 
        map[nums[i]] = i
    return None

def main():
    # Test cases
    test_cases = [
        ([2, 7, 11, 15], 9),
        ([3, 2, 4], 6),
        ([3, 3], 6),
    ]
    
    for nums, target in test_cases:
        result = TwoSum2(nums, target)
        print(f"nums: {nums}, target: {target} -> {result}")

if __name__ == "__main__":
    main()  