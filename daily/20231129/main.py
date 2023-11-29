class Solution:
    def hammingWeight(self, n: int) -> int:
        n = bin(n)
        return len(list(filter(lambda i: i == "1", n)))


solution = Solution()

testcases = [
    0o00000000000000000000000000001011,
    0o00000000000000000000000010000000,
    0o11111111111111111111111111111101,
]  # Input
outputs = [3, 1, 31]  # Output

for index, testcase in enumerate(testcases):
    response = solution.hammingWeight(testcase)
    if response == outputs[index]:
        print(f"Case #{index}: Succeeded")
    else:
        print(f"Case #{index}: Failed")
