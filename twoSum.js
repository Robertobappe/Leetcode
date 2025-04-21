function twoSum (nums, target){
    map = {};
    for(let i=0; i<nums.length; i++){
        comp = target - nums[i];
        
        if(map[target - nums[i]]){
            return [nums.indexOf(comp),i]; 
        }
        if(!map[comp]){
            map[nums[i]] = true; 
        }
    }
}

console.log(twoSum([2,7,11,15], 9))