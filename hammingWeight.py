class Solution:
    def hammingWeight(self, n: int) -> int:
        # My solution
        # Space complexity O(32 btis) = O(c), where c is a constant
        # Verify each bit
        binaryNumber = bin(n)[2:]
        sumOne = 0

        # Time complexity  O(32 btis) = O(c)
        for i in range(len(binaryNumber)):
            if binaryNumber[i] == '1':
                sumOne += 1
            
        return sumOne
    

        # Another solution 1
        # Verify each bit
        '''
        res = 0
        while n:
            res += n % 2
            n = n >> 1
        return res'''
    
    
        # Another solution 2: most efficient
        # Verify just the 1 bit
        '''
        res = 0 
        while n:
            n &= (n - 1)
            res += 1
        return res'''    


def main():
    tests_cases = [
        11, 128,2147483645
    ]

    for i in tests_cases:
        sol = Solution()
        rel = sol.hammingWeight(i)
        print(f'Input {i} Output {rel}')

if __name__ == '__main__':
    main()