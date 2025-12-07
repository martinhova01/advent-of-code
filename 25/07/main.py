import time
from collections import deque
from functools import cache


class Solution:
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = open(self.filename).read().rstrip().split("\n")

    def part1(self):
        R = len(self.data)
        C = len(self.data[0])

        start = None
        for y in range(R):
            for x in range(C):
                c = self.data[y][x]
                if c == "S":
                    start = (x, y)

        q = deque([start])
        visited = set()
        splits = 0
        while q:
            x, y = q.popleft()

            if (x, y) in visited:
                continue
            visited.add((x, y))

            nx, ny = x, y + 1

            if ny >= R:
                continue

            if self.data[ny][nx] == "^":
                splits += 1

                if nx + 1 < C:
                    q.append((nx + 1, ny))
                if nx - 1 >= 0:
                    q.append((nx - 1, ny))
            else:
                q.append((nx, ny))

        return splits

    @cache
    def num_paths(self, x, y):

        nx, ny = x, y + 1
        if ny >= self.R:
            return 1

        if self.data[ny][nx] == "^":

            s = 0
            if nx + 1 < self.C:
                s += self.num_paths(nx + 1, ny)
            if nx - 1 >= 0:
                s += self.num_paths(nx - 1, ny)
            return s
        else:
            return self.num_paths(nx, ny)

    def part2(self):
        self.R = len(self.data)
        self.C = len(self.data[0])

        start = None
        for y in range(self.R):
            for x in range(self.C):
                c = self.data[y][x]
                if c == "S":
                    start = (x, y)

        return self.num_paths(start[0], start[1])


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
