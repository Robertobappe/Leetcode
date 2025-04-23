function rotate(nums,k){
    k = k % nums.length;
    console.log('valor de k '+ k);

    nums.reverse();
    revNums(nums,0,k-1);
    revNums(nums,k,nums.length-1);
}

function revNums(nums,start,end){
    while(start < end){
        [nums[start], nums[end]] = [nums[end],nums[start]];
        start++;
        end--;
    }
}