//Brute force
function maxSubArray(nums){
    if(nums.length == 1){
        return nums[0];
    }
    const arr = [0];
    let soma = 0;

    for(let i=0; i < nums.length - 1;i++){
        let somaj = 0;
        for(let j=i+1; j < nums.length;j++){
            somaj += nums[j];
            soma = nums[i] + somaj; 
            if(arr[0] == '' || soma > arr[0]){
                arr[0] = soma; 
            }
        }
    }
    return arr[0];
}
console.log(maxSubarray([-2,1,-3,4,-1,2,1,-5,4]));

//nums[i] = 4
//nums[j] = -1