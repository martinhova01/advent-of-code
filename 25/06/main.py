import time
import itertools
import functools
from collections import Counter, defaultdict, deque
import networkx as nx
from tqdm import tqdm
import numpy as np
import re
import copy
from functools import cache

import sys

sys.path.append("../..")
from utils import adjacent4, adjacent8, directions4, directions8, manhattanDist


class Solution:
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = [
            list(map(int, re.findall(r"-?\d+", line)))
            for line in open(self.filename).read().rstrip().split("\n")
        ][:-1]
        self.operations = (
            open(self.filename).read().rstrip().split("\n")[-1].replace(" ", "")
        )

    def part1(self):
        Y = len(self.data)
        X = len(self.data[0])

        tot = 0
        for x in range(X):
            res = None
            if self.operations[x] == "*":
                res = 1
            else:
                res = 0
            for y in range(Y):
                if self.operations[x] == "*":
                    res *= self.data[y][x]
                else:
                    res += self.data[y][x]
            tot += res

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
                if c.isnumeric():
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

        tot += tmp

        return tot

        # transposed = np.transpose(self.data).tolist()
        # print(transposed)

        # tot = 0
        # for i, col in enumerate(transposed):
        #     length = 0
        #     for num in col:
        #         length = max(length, len(str(num)))
        #     if self.operations[i] == "*":
        #         res = 1
        #     else:
        #         res = 0
        #     for j in range(length):
        #         num = ""
        #         for n in col:
        #             n = str(n)
        #             if len(n) < j + 1:
        #                 continue
        #             num += n[-1 -j]

        #         num = int(num)

        #         print(num)
        #         if self.operations[i] == "*":
        #             res *= num
        #         else:
        #             res += num

        #     print(res)

        #     tot += res

        # return tot


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
