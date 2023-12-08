from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root:
            curr_str = f"{str(root.val)}"

            if root.left:
                curr_str += f"({self.tree2str(root.left)})"
            else:
                if root.right:
                    curr_str += "()"

            if root.right:
                curr_str += f"({self.tree2str(root.right)})"

            return curr_str
        else:
            return ""


solution = Solution()

testcases = [
    TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3)),
    TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3)),
]  # Input
outputs = ["1(2(4))(3)", "1(2()(4))(3)"]  # Output

for index, testcase in enumerate(testcases):
    response = solution.tree2str(testcase)
    print(response)
    if response == outputs[index]:
        print(f"Case #{index}: Succeeded")
    else:
        print(f"Case #{index}: Failed")
