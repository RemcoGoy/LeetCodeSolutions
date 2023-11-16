class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        SPECIAL_CHARS = "!@#$%^&*()-+"

        n = len(password)
        uppercase_flag = False
        lowercase_flag = False
        special_character_flag = False
        digit_flag = False

        if n < 8:
            return False

        prev_char = None
        for i in range(n):
            curr_char = password[i]

            if prev_char:
                if prev_char == curr_char:
                    return False

            uppercase_flag = curr_char.isupper() or uppercase_flag
            lowercase_flag = curr_char.islower() or lowercase_flag
            digit_flag = curr_char.isdigit() or digit_flag
            special_character_flag = (
                curr_char in SPECIAL_CHARS or special_character_flag
            )

            prev_char = curr_char

        return (
            uppercase_flag and lowercase_flag and special_character_flag and digit_flag
        )


solution = Solution()

testcases = ["IloveLe3tcode!", "Me+You--IsMyDream", "1aB!"]
outputs = [True, False, False]

for index, testcase in enumerate(testcases):
    response = solution.strongPasswordCheckerII(testcase)
    if response == outputs[index]:
        print(f"Case #{index}: Succeeded")
    else:
        print(f"Case #{index}: Failed")
