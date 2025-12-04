import time
import copy

import sys

sys.path.append("../..")
from utils import adjacent8


class Solution:
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = [
            list(line) for line in open(self.filename).read().rstrip().split("\n")
        ]
        self.R = len(self.data)
        self.C = len(self.data[0])

    def part1(self):

        res = 0
        for y in range(self.R):
            for x in range(self.C):
                if self.data[y][x] != "@":
                    continue

                s = 0
                for nx, ny in adjacent8(x, y):
                    if nx < 0 or nx >= self.C or ny < 0 or ny >= self.R:
                        continue
                    if self.data[ny][nx] == "@":
                        s += 1
                if s < 4:
                    res += 1

        return res

    def part2(self):

        res = 0
        updated = True
        while updated:
            new_data = copy.deepcopy(self.data)
            updated = False

            for y in range(self.R):
                for x in range(self.C):
                    if self.data[y][x] != "@":
                        continue

                    s = 0
                    for nx, ny in adjacent8(x, y):
                        if nx < 0 or nx >= self.C or ny < 0 or ny >= self.R:
                            continue
                        if self.data[ny][nx] == "@":
                            s += 1
                    if s < 4:
                        updated = True
                        new_data[y][x] = "."
                        res += 1

                self.data = new_data

        return res


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
