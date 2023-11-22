from collections import deque
from itertools import chain
from typing import List


class Solution:
    def findDiagonalOrder(self, nums):
        diagonals = [deque() for _ in range(len(nums) + max(len(row) for row in nums) - 1)]
        for row_id, row in enumerate(nums):
            for col_id in range(len(row)):
                diagonals[row_id + col_id].appendleft(row[col_id])
        return list(chain(*diagonals))


solution = Solution()

testcases = [
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[1, 2, 3, 4, 5], [6, 7], [8], [9, 10, 11], [12, 13, 14, 15, 16]],
]  # Input
outputs = [
    [1, 4, 2, 7, 5, 3, 8, 6, 9],
    [1, 6, 2, 8, 7, 3, 9, 4, 12, 10, 5, 13, 11, 14, 15, 16],
]  # Output

for index, testcase in enumerate(testcases):
    response = solution.findDiagonalOrder(testcase)
    if response == outputs[index]:
        print(f"Case #{index}: Succeeded")
    else:
        print(f"Case #{index}: Failed")
