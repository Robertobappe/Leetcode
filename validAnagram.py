class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        #Solution
        """        
        mapS,mapT = {}, {}

        for i in range(len(s)):
            mapS[s[i]] = 1 + mapS.get(s[i], 0)
            mapT[t[i]] = 1 + mapT.get(t[i], 0)
        
        return mapS == mapT """
        #Dicionários em Python são Comparados por Conteúdo, Não por Ordem        
        #Time complexity O(n)
        #Space complexity O(k) --> since we have at most 26 different characters 
    
        #Other solution
        """
        return sorted(s) == sorted(t)
        """
        #Time complexity O(nlogn)
        #Space complexity O(1) or O(n)

        #Other solution
        from collections import Counter
        #cria um dicionário que mapeia cada caractere de s ao seu número de ocorrências
        return Counter(s) == Counter(t)
        #Time Complexity O(n)
        #Space Complexity O(k)

sol = Solution() # Step 1: Create an instance
result = sol.isAnagram("anagram","nagaram")
print(result)