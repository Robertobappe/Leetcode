from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupAnagram = []
        if len(strs) == 1:
            groupAnagram.append(strs)
            return groupAnagram            
        
        for i in range(len(strs) - 1):
            listAnagram = []
            
            for j in range(i+1, len(strs)):
                result = Solution().isValidAnagram(strs[i], strs[j])
                if result:
                    if not strs[i] in listAnagram:
                        listAnagram.append(strs[i])
                    listAnagram.append(strs[j])
            
            if len(listAnagram) > 0:
                groupAnagram.append(listAnagram)

        return groupAnagram

    def isValidAnagram(self, s:str, t:str):
        if len(s) != len(t):
            return False
            
        sMap, tMap = {}, {}

        for i in range(len(s)):
            sMap[s[i]] = 1 + sMap.get(s[i], 0)
            tMap[t[i]] = 1 + tMap.get(t[i], 0)
            
        return sMap == tMap
    

def main():
    test_cases = [
        ["eat","tea","tan","ate","nat","bat"],
        [""],
        ["a"]
    ]

    for i in test_cases:
        res = Solution().groupAnagrams(i)
        print(f'Input {i} Output {res}')

if __name__ == '__main__':
    main()

