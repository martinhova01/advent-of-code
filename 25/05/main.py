import time


class Solution:
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = self.parse(open(self.filename).read().rstrip())

    def parse(self, data: str):
        _ranges, ind = data.split("\n\n")

        ranges = []
        for line in _ranges.split("\n"):
            start, stop = line.split("-")
            ranges.append(range(int(start), int(stop) + 1))

        items = list(map(int, ind.split("\n")))

        self.ranges: list[range] = ranges
        self.items = items

    def part1(self):
        res = 0
        for item in self.items:
            if any(item in r for r in self.ranges):
                res += 1
        return res

    def part2(self):

        intervals = [(r.start, r.stop) for r in self.ranges]
        intervals.sort()
        merged = []

        cur_start, cur_stop = intervals[0]

        for start, stop in intervals[1:]:
            if start <= cur_stop:
                # extend current interval
                cur_stop = max(cur_stop, stop)
            else:
                # make new interval
                merged.append(range(cur_start, cur_stop))
                cur_start, cur_stop = start, stop

        merged.append(range(cur_start, cur_stop))

        return sum(r.stop - r.start for r in merged)


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
