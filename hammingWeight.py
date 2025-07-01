class Solution:
    def hammingWeight(self, n: int) -> int:
        binaryNumber = bin(n)[2:]
        sumOne = 0

        for i in range(len(binaryNumber)):
            if binaryNumber[i] == '1':
                sumOne += 1
            
        return sumOne
    


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