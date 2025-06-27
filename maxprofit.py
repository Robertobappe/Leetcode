from typing import List

class solution:
    # Brute force --> Time O(n^2) and space O(1)
    def maxProfit(self, prices: List[int]) -> int:
        '''maxProfit = 0
        for i in range(len(prices) - 1):
            for j in range(i+1, len(prices)):
                if prices[j] - prices[i] > 0 and prices[j] - prices[i] > maxProfit:
                    maxProfit = prices[j] - prices[i]

        return maxProfit if maxProfit else 0'''

        maxProfit = 0 
        left, right = 0, 1
        n = len(prices)

        while right < n: 
            profit = prices[right] - prices[left]
            if profit > 0:
                right += 1
                if profit > maxProfit:
                    maxProfit = profit
            else:
                left = right
                right += 1 
        
        return maxProfit if maxProfit else 0

    
def main():
    tests_cases = [
        [7,1,5,3,6,4],[7,6,4,3,1]
    ]

    for k in tests_cases:
        sol = solution()
        rel = sol.maxProfit(k)
        print(f'Input {k} Output {rel}')

if __name__ == '__main__':
    main()