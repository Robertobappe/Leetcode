class Solution:
    def climbStairs(self, n: int) -> int:
        # Recursion 
        # Time complexity O(2^n)
        # Space complexity O(n)
        '''
        if n < 1:
            return None
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)'''


        # Top down Memoization
        # Time complexity O(n)
        # Space complexity O(n)
        '''
        memo = {1:1, 2:2}
        def f(n):
            if n in memo:
                return memo[n]
            else:
                memo[n] = f(n-1) + f(n-2)
                return memo[n]
        
        return f(n)'''


        # Botton up Tabulation
        # Time complexity O(n)
        # Space complexity O(n)
        '''
        if n == 1:
            return 1
        elif n == 2:
            return 2
        
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2

        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n-1]'''


        # Botton up constant space
        # Time complexity O(n)
        # Space complexity O(1)
        if n == 1:
            return 1
        elif n == 2:
            return 2
        
        prev, cur = 1, 2
        for i in range(2, n):
            prev, cur = cur, cur + prev

        return cur




def main():
    tests_cases = [1,2,3,4,5,6,7,8,9]

    for i in tests_cases:
        sol = Solution()
        rel = sol.climbStairs(i)
        print(f'Input n={i} Output {rel}')

if __name__ == '__main__':
    main()



