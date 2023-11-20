class Solution:
    def method(self):
        pass


solution = Solution()

testcases = []  # Input
outputs = []  # Output

for index, testcase in enumerate(testcases):
    response = solution.method()
    if response == outputs[index]:
        print(f"Case #{index}: Succeeded")
    else:
        print(f"Case #{index}: Failed")
