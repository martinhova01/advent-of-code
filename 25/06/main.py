import time
import functools
import numpy as np
import re


class Solution:
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"

    def part1(self):
        data = [
            list(map(int, re.findall(r"-?\d+", line)))
            for line in open(self.filename).read().rstrip().split("\n")
        ][:-1]
        
        operations = (
            open(self.filename).read().rstrip().split("\n")[-1].replace(" ", "")
        )
        
        tot = 0
        transposed = np.transpose(data).tolist()
        for i, col in enumerate(transposed):
            if operations[i] == "*":
                tot += functools.reduce(lambda x, y: x * y, col)
            else:
                tot += sum(col)

        return tot

    def part2(self):
        data = open(self.filename).read().split("\n")
        Y = len(data)
        X = len(data[0])
        op = None
        tot = 0
        tmp = -1

        for x in range(X):
            if all(data[y][x] == " " for y in range(Y)):
                tot += tmp
                tmp = -1
                continue

            num = ""
            for y in range(Y):
                c = data[y][x]
                if c == " ":
                    continue
                elif c.isnumeric():
                    num += c
                else:
                    op = c

            num = int(num)
            if tmp == -1:
                tmp = num
            else:
                if op == "*":
                    tmp *= num
                else:
                    tmp += num

        # last number is not added since there are no empty column at the end
        tot += tmp
        
        return tot


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
