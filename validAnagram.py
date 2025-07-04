class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Time complexity O(n)
        #Space complexity O(k) --> since we have at most 26 different characters 
        if len(s) != len(t):
            return False
        
        #Solution     
        mapS,mapT = {}, {}

        for i in range(len(s)):
            mapS[s[i]] = 1 + mapS.get(s[i], 0)
            mapT[t[i]] = 1 + mapT.get(t[i], 0)
        
        return mapS == mapT 
    

def main():
    tests_cases = [
        ("anagram","nagaram"),
        ("rat","car")
    ]
    
    for s_input,t_input in tests_cases:
        sol = Solution()
        res = sol.isAnagram(s_input,t_input)
        print(f'Input {s_input} e {t_input} Output {res}')

if __name__ == '__main__':
    main()