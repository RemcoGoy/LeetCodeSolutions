from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ans = ""

        for i, num in enumerate(nums):
            ans += "1" if (num[i] == "0") else "0"

        return ans


solution = Solution()

testcases = [["01", "10"], ["00", "01"], ["111", "011", "001"]]
outputs = [["11", "00"], ["11", "10"], ["101", "000", "010", "100", "110"]]

for index, testcase in enumerate(testcases):
    response = solution.findDifferentBinaryString(testcase)
    if response in outputs[index]:
        print(f"Case #{index}: Succeeded")
    else:
        print(f"Case #{index}: Failed")
