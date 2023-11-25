from typing import List


class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        res = []

        prefix_sum = 0
        suffix_sum = sum(nums)

        for i, num in enumerate(nums):
            left_sum = num * i - prefix_sum

            right_sum = suffix_sum - num * (len(nums) - i)

            total_sum = left_sum + right_sum

            res.append(total_sum)

            prefix_sum += num
            suffix_sum -= num

        return res


solution = Solution()

testcases = [[2, 3, 5], [1, 4, 6, 8, 10]]  # Input
outputs = [[4, 3, 5], [24, 15, 13, 15, 21]]  # Output

for index, testcase in enumerate(testcases):
    response = solution.getSumAbsoluteDifferences(testcase)
    if response == outputs[index]:
        print(f"Case #{index}: Succeeded")
    else:
        print(f"Case #{index}: Failed")
