import time
from collections import deque
import re
import pulp


class Solution:
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = [
            self.parse_line(line)
            for line in open(self.filename).read().rstrip().split("\n")
        ]

    def parse_line(self, line):
        square = re.search(r"\[(.*?)\]", line).group(1)

        parens = []
        for grp in re.findall(r"\((.*?)\)", line):
            nums = tuple(int(x) for x in grp.split(",")) if grp else ()
            parens.append(nums)

        curly = [int(x) for x in re.search(r"\{(.*?)\}", line).group(1).split(",")]

        return square, parens, curly

    def get_num_presses(self, goal: int, buttons: list[int]) -> int:

        visited = set()
        q = deque([(0, 0)])  # indicator, clicks

        while q:

            indicators, clicks = q.popleft()
            if indicators in visited:
                continue
            visited.add(indicators)

            if indicators == goal:
                return clicks

            for button in buttons:
                next_indicators = indicators ^ button

                q.append((next_indicators, clicks + 1))

    def part1(self):
        s = 0
        for indicators, buttons, _ in self.data:
            indicators = int(indicators.replace("#", "1").replace(".", "0")[::-1], 2)

            new_buttons = []
            for button in buttons:
                button = int(
                    "".join(
                        reversed(
                            [
                                "1" if i in button else "0"
                                for i in range(max(button) + 1)
                            ]
                        )
                    ),
                    2,
                )
                new_buttons.append(button)
            buttons = new_buttons
            s += self.get_num_presses(indicators, buttons)
        return s

    def part2(self):
        s = 0
        for _, buttons, joltage in self.data:

            A = []
            for i in range(len(joltage)):
                line = []
                for button in buttons:
                    if i in button:
                        line.append(1)
                    else:
                        line.append(0)
                A.append(line)

            b = joltage
            num_buttons = len(buttons)

            prob = pulp.LpProblem("ButtonPresses", pulp.LpMinimize)
            x_vars = [
                pulp.LpVariable(f"x{i}", lowBound=0, cat="Integer")
                for i in range(num_buttons)
            ]

            # objective
            prob += pulp.lpSum(x_vars)

            # Add equality constraints
            for row_idx, row in enumerate(A):
                prob += (
                    pulp.lpSum(row[j] * x_vars[j] for j in range(num_buttons))
                    == b[row_idx]
                )

            prob.solve(pulp.PULP_CBC_CMD(msg=False))

            s += sum([x.value() for x in x_vars])
        return int(s)


def main():
    start = time.perf_counter()

    s = Solution(test=True)
    print("---TEST---")
    print(f"part 1: {s.part1()}")
    print(f"part 2: {s.part2()}\n")

    s = Solution()
    print("---MAIN---")
    print(f"part 1: {s.part1()}")
    print(f"part 2: {s.part2()}")

    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")


main()
