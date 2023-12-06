class Solution:
    def weekvalue(self, start: int):
        total = 0
        for i in range(7):
            total += start + i
        return total

    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        days = n % 7

        curr_start = 1

        total = 0

        for i in range(weeks):
            total += self.weekvalue(curr_start)
            curr_start += 1

        for i in range(days):
            total += curr_start + i

        return total


solution = Solution()

testcases = [4, 10, 20]  # Input
outputs = [10, 37, 96]  # Output

for index, testcase in enumerate(testcases):
    response = solution.totalMoney(testcase)
    if response == outputs[index]:
        print(f"Case #{index}: Succeeded")
    else:
        print(f"Case #{index}: Failed")
