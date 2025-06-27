import re

class solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''

        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]


def main():
    tests_cases = [
        "A man, a plan, a canal: Panama","race a car" 
    ]

    for i in tests_cases:
        sol = solution()
        rel = sol.isPalindrome(i)
        print(rel)

if __name__ == '__main__':
    main()
