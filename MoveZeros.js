
//brute force
function moveZeroes (nums){
    let arrZeros = [];
    let arrNums = [];
    for(let i=0; i < nums.length; i++){
        if(nums[i] == 0){
            arrZeros.push(nums[i]);
        }else{
            arrNums.push(nums[i]);
        }
    }
    arrNums = arrNums.concat(arrZeros);
    return arrNums;
}

function moveZeroes2(nums){
    let j = 0;
    let aux = 0;
    for(let i=0; i < nums.length; i++){          
        if(nums[i] != 0){
            aux = nums[i];
            nums[i] = nums[j];
            nums[j] = aux;
            j++;
        }
    }
    return nums;
}

console.log(moveZeroes2([0,0,0,0,0,0,1,1,1]));