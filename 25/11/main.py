import time
import networkx as nx
from collections import defaultdict
from functools import cache


class Solution:
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = open(self.filename).read().rstrip().split("\n")

    def part1(self):
        G = nx.DiGraph()
        for line in self.data:
            start, ends = line.split(": ")
            for end in ends.split(" "):
                G.add_edge(start, end)

        return len(list(nx.all_simple_paths(G, "you", "out")))

    @cache
    def num_paths(self, start, end, fft: bool, dac: bool):
        if start == end:
            return fft and dac

        nxt_fft, nxt_dac = fft, dac
        if start == "fft":
            nxt_fft = True

        if start == "dac":
            nxt_dac = True

        s = 0
        for nxt in self.G[start]:
            s += self.num_paths(nxt, end, nxt_fft, nxt_dac)
        return s

    def part2(self):
        self.G = defaultdict(list)
        for line in self.data:
            start, ends = line.split(": ")
            for end in ends.split(" "):
                self.G[start].append(end)

        return self.num_paths("svr", "out", False, False)


def main():
    start = time.perf_counter()

    s = Solution(test=True)
    print("---TEST---")
    print(f"part 2: {s.part2()}\n")

    s = Solution()
    print("---MAIN---")
    print(f"part 1: {s.part1()}")
    print(f"part 2: {s.part2()}")

    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")


main()
