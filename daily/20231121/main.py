from typing import List


class Solution:
    def revNumber(self, x: int) -> int:
        return int("".join([i for i in str(x)][::-1]))

    def countNicePairs(self, nums: List[int]) -> int:
        mod = 1000000007

        nums = [num - self.revNumber(num) for num in nums]
        nums.sort()

        res = 0
        i = 0
        while i < len(nums) - 1:
            cont = 1
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                cont += 1
                i += 1
            res = (res % mod + (cont * (cont - 1)) // 2) % mod
            i += 1

        return int(res % mod)


solution = Solution()

testcases = [[42, 11, 1, 97], [13, 10, 35, 24, 76]]  # Input
outputs = [2, 4]  # Output

for index, testcase in enumerate(testcases):
    response = solution.countNicePairs(testcases[index])
    if response == outputs[index]:
        print(f"Case #{index}: Succeeded")
    else:
        print(f"Case #{index}: Failed")
