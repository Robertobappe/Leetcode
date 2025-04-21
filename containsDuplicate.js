//My solution
function containsDuplicate(nums){
    let map = {};
    for(let i=0; i<nums.length; i++){
        if(map[nums[i]]){
            return true;
        }
        if(!map[nums[i]]){
            map[nums[i]] = true;
        }
    }
    return false;
}

//Better solution
function containsDuplicate2(nums){
    const map = {};
    for(let i=0; i<nums.length; i++){
        if (map[nums[i]]){
            return true;
        }
        map[nums[i]] = true;
    }
    return false;
}
// há como melhorar?
console.log(containsDuplicate([1,1,1,3,3,4,3,2,4,2]));
