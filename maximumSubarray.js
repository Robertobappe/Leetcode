//Brute force --> 
function maxSubArray(nums){
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

//Better solution
function maxSubArray2(nums){
    let curSum = nums[0]; 
    let maxSub = nums[0]; 

    if(nums.length == 1){
        return nums[0];
    }     
    for (let i=1; i < nums.length; i++){
        curSum = Math.max(nums[i], nums[i] + curSum);
        maxSub = Math.max(maxSub, curSum);  
    }
    return maxSub;
}
console.log(maxSubArray2([-2,1,-3,4,-1,2,1,-5,4]));