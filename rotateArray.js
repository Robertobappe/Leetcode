/*
function rotate(nums, k){
   for(let i=0; i<k; i++){
        //pop() removes the last element from an array
        //unshift() adds the specified elements to the 
        //beginning of an array
        nums.unshift(nums.pop());
    }
    return nums;
}

console.log(rotate([-1,-100,3,99],2));
*/

function rotate(nums,k){
    let arr1 = nums.slice(0,nums.length - k);
    const arr2 = nums.slice(nums.length - k,nums.length);
    return arr2.concat(arr1);
}
console.log(rotate([1,2,3,4,5,6,7],3));