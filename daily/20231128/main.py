class Solution:
    def numberOfWays(self, corridor):
        x = 1  # 0 seat
        y = 0  # 1 seat
        z = 0  # 2 seats
        for char in corridor:
            print(char)
            if char == "S":
                x, y, z = 0, x + z, y
            else:
                x, y, z = x + z, y, z

            print(x, y, z)
        return z % (10**9 + 7)


solution = Solution()

testcases = ["SSPPSPS", "PPSPSP", "S"]  # Input
outputs = [3, 1, 0]  # Output

for index, testcase in enumerate(testcases):
    response = solution.numberOfWays(testcase)
    if response == outputs[index]:
        print(f"Case #{index}: Succeeded")
    else:
        print(f"Case #{index}: Failed")
