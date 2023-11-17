from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()

        curr_max = -1
        for i in range(int(len(nums) / 2)):
            front_index = i
            back_index = len(nums) - 1 - i

            x = nums[front_index]
            y = nums[back_index]

            curr = x + y
            if curr > curr_max:
                curr_max = curr

        return curr_max


solution = Solution()

testcases = [[3, 5, 2, 3], [3, 5, 4, 2, 4, 6]]
outputs = [7, 8]

for index, testcase in enumerate(testcases):
    response = solution.minPairSum(testcase)
    if response == outputs[index]:
        print(f"Case #{index}: Succeeded")
    else:
        print(f"Case #{index}: Failed")
