function groupAnagrams(strs){
    let map={};
    let aux = '';

    for(let i=0; i<strs.length; i++){
        aux = strs[i].split("").sort().join("");
        //console.log('strs[i] ' + strs[i]);
        //console.log('aux ' + aux);
        if(!map[aux]){
            map[aux] = [strs[i]];
        }
        else{
            map[aux].push(strs[i]);
        }        
    }
    return Object.values(map);
}

console.log(groupAnagrams(["eat","tea","tan","ate","nat","bat"]));