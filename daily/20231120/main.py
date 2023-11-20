from typing import List


class Solution:
    """
    print scale(0, (0.0, 99.0), (-1.0, +1.0))
    print scale(1, (0.0, 99.0), (-1.0, +1.0))
    print scale(99, (0.0, 99.0), (-1.0, +1.0))
    """

    def scale(self, val, src, dst):
        return ((val - src[0]) / (src[1] - src[0])) * (dst[1] - dst[0]) + dst[0]

    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        trucks = ["G", "P", "M"]
        total = 0
        for truck in trucks:
            truck_total = 0

            if truck in "".join(garbage):
                reverse = garbage

            total += truck_total

        return total


solution = Solution()

testcases = [[["G", "P", "GP", "GG"], [2, 4, 3]], [["MMM", "PGM", "GP"], [3, 10]]]  # Input
outputs = [21, 37]  # Output

for index, testcase in enumerate(testcases):
    response = solution.garbageCollection(testcases[index][0], testcases[index][1])
    print(response)
    if response == outputs[index]:
        print(f"Case #{index}: Succeeded")
    else:
        print(f"Case #{index}: Failed")
