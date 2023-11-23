from typing import List


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []

        for i in range(len(l)):
            seq = nums[l[i] : r[i] + 1]
            seq.sort()

            prev_diff = None
            good_seq = True
            for j in range(len(seq)):
                if j < len(seq) - 1:
                    curr = seq[j]
                    nxt = seq[j + 1]

                    diff = nxt - curr
                    if prev_diff == 0 or prev_diff:
                        if not diff == prev_diff:
                            good_seq = False
                            break

                    prev_diff = diff

            res.append(good_seq)

        return res


solution = Solution()

testcases = [
    [[4, 6, 5, 9, 3, 7], [0, 0, 2], [2, 3, 5]],
    [[-12, -9, -3, -12, -6, 15, 20, -25, -20, -15, -10], [0, 1, 6, 4, 8, 7], [4, 4, 9, 7, 9, 10]],
]  # Input
outputs = [[True, False, True], [False, True, False, False, True, True]]  # Output

for index, testcase in enumerate(testcases):
    response = solution.checkArithmeticSubarrays(testcase[0], testcase[1], testcase[2])
    if response == outputs[index]:
        print(f"Case #{index}: Succeeded")
    else:
        print(f"Case #{index}: Failed")
