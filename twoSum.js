function twoSum (nums, target){
    map = {};
    index = [];
    for(let i=0; i<nums.length; i++){
        comp = target - nums[i];
        
        if(map[target - nums[i]]){
            index.push(nums.indexOf(comp));
            index.push(i);
            return index; 
        }
        if(!map[comp]){
            map[nums[i]] = true; 
        }
    }
}

console.log(twoSum([2,7,11,15], 9))