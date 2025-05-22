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


print(TwoSum2([2,7,11,15],9))
print(TwoSum2([3,2,4],6))
print(TwoSum2([3,3],6))