from typing import List


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        res = 0
        piles.sort()

        for i in range(int(len(piles) / 3)):
            # Alice
            piles.pop(len(piles) - 1)

            # Me
            res += piles.pop(len(piles) - 1)

            # Bob
            piles.pop(0)

        return res


solution = Solution()

testcases = [[2, 4, 1, 2, 7, 8], [2, 4, 5], [9, 8, 7, 6, 5, 1, 2, 3, 4]]  # Input
outputs = [9, 4, 18]  # Output

for index, testcase in enumerate(testcases):
    response = solution.maxCoins(testcase)
    if response == outputs[index]:
        print(f"Case #{index}: Succeeded")
    else:
        print(f"Case #{index}: Failed")
