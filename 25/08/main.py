import time
import functools


class Solution:
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = [
            tuple(map(int, line.split(",")))
            for line in open(self.filename).read().rstrip().split("\n")
        ]

    def dist(self, a, b):
        return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2) ** 0.5

    def part1(self):
        distances = {}
        for i in range(len(self.data)):
            for j in range(i + 1, len(self.data)):
                p, q = self.data[i], self.data[j]
                distances[(p, q)] = self.dist(p, q)

        circuits = [{x} for x in self.data]

        N = 10 if self.test else 1000
        for (p, q), _ in sorted(distances.items(), key=lambda item: item[1])[:N]:

            i_p, i_q = -1, -1
            for i, cir in enumerate(circuits):
                if p in cir:
                    i_p = i
                if q in cir:
                    i_q = i

            if i_p == i_q:
                continue

            circuits[i_p] = circuits[i_p].union(circuits[i_q])
            circuits.pop(i_q)

        lens = sorted(map(len, circuits), reverse=True)
        return functools.reduce(lambda x, y: x * y, lens[:3])

    def part2(self):
        distances = {}
        for i in range(len(self.data)):
            for j in range(i + 1, len(self.data)):
                p, q = self.data[i], self.data[j]
                distances[(p, q)] = self.dist(p, q)

        circuits = [{x} for x in self.data]
        for (p, q), _ in sorted(distances.items(), key=lambda item: item[1]):

            i_p, i_q = -1, -1
            for i, cir in enumerate(circuits):
                if p in cir:
                    i_p = i
                if q in cir:
                    i_q = i

            if i_p == i_q:
                continue

            circuits[i_p] = circuits[i_p].union(circuits[i_q])
            circuits.pop(i_q)

            if len(circuits) == 1:
                return p[0] * q[0]


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
