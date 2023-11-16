from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print(self):
        curr_print = f"{self.val}"
        if self.next:
            return f"{curr_print} => {self.next.print()}"
        else:
            return curr_print


class Solution:
    def linkedToInverseNumber(self, l: Optional[ListNode]):
        res_array = []
        while l != None:
            res_array.append(l.val)
            if l.next:
                l = l.next
            else:
                l = None

        return int("".join(map(str, res_array[::-1])))

    def numberToInverseLinked(self, n: int):
        l = None
        for x in [int(x) for x in str(n)]:
            if l:
                l = ListNode(x, l)
            else:
                l = ListNode(x)

        return l

    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        n1 = self.linkedToInverseNumber(l1)
        n2 = self.linkedToInverseNumber(l2)

        n3 = n1 + n2

        return self.numberToInverseLinked(n3)


solution = Solution()


l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))

l3 = ListNode(0)
l4 = ListNode(0)

l5 = ListNode(
    9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))
)
l6 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))

testcases = [
    [l1, l2],
    [l3, l4],
    [l5, l6],
]  # Input
outputs = [
    ListNode(7, ListNode(0, ListNode(8))),
    ListNode(0),
    ListNode(
        8,
        ListNode(
            9,
            ListNode(
                9, ListNode(9, ListNode(0, ListNode(0, ListNode(0, ListNode(1)))))
            ),
        ),
    ),
]  # Output


def compareList(a: ListNode, b: ListNode):
    if a.val != b.val:
        return False

    if b.next != None and a.next != None:
        return compareList(a.next, b.next)
    else:
        if b.next != a.next:
            return False
        else:
            return True


for index, testcase in enumerate(testcases):
    response = solution.addTwoNumbers(testcase[0], testcase[1])
    if response and compareList(response, outputs[index]):
        print(f"Case #{index}: Succeeded")
    else:
        print(f"Case #{index}: Failed")
