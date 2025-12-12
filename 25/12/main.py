import time
from collections import defaultdict
import re
from functools import cache


class Solution:
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = self.parse(open(self.filename).read().rstrip())

    def parse(self, data: str):
        sections = data.split("\n\n")
        presents = defaultdict(set)
        for i, section in enumerate(sections[:-1]):
            for row, line in enumerate(section.split("\n")):
                if ":" in line:
                    continue
                for x in range(len(line)):
                    if line[x] == "#":
                        presents[i].add((x, row - 1))

        areas = []

        for line in sections[-1].split("\n"):
            nums = list(map(int, re.findall(r"\d+", line)))
            areas.append(((nums[0], nums[1]), nums[2:]))

        self.presents = presents
        self.areas = areas

    def rotate(self, present: set[tuple[int, int]]):
        new_present = set()
        for x, y in present:
            new_present.add((y, -x))
        return new_present

    def flip(self, present: set[tuple[int, int]]):
        new_present = set()
        for x, y in present:
            new_present.add((-x, y))
        return new_present

    # @cache
    # def fits(self, w, l, num_presents, used):

    #     if all(num_present == 0 for num_present in num_presents):
    #         return True

    #     i = -1
    #     for j, num in enumerate(num_presents):
    #         if num > 0:
    #             i = j
    #             break

    #     new_num_presents = list(num_presents)
    #     new_num_presents[i] -= 1

    #     present = self.presents[i]

    #     for y in range(l):
    #         for x in range(w):
    #             if (x, y) in used:
    #                 continue
    #             for rot in range(4):
    #                 present = self.rotate(present)
    #                 for flip in range(2):
    #                     present = self.flip(present)
    #                     new_used: set = set(used)

    #                     if any(x + dx < 0 or x + dx >= w or y + dy < 0 or y + dy >= l for dx, dy in present):
    #                         continue

    #                     if all((x + dx, y + dy ) not in new_used for dx, dy in present):
    #                         new_used.update({(x + dx, y + dy) for dx, dy in present})

    #                         fits = self.fits(w, l, tuple(new_num_presents), tuple(new_used))
    #                         if fits:
    #                             return True

    #     return False

    def part1(self):

        # s = 0
        # for area in self.areas:
        #     (w, l), num_presents = area
        #     if self.fits(w, l, tuple(num_presents), ()):
        #         print(area)
        #         s += 1

        # return s
        s = 0
        for area in self.areas:
            (w, l), num_presents = area
            size = w * l
            pres_sum = 0
            for i, num_present in enumerate(num_presents):
                pres_sum += len(self.presents[i]) * num_present

            if size < pres_sum:
                continue
            s += 1

        return s

    def part2(self):
        return None


def main():
    start = time.perf_counter()

    s = Solution()
    print("---MAIN---")
    print(f"part 1: {s.part1()}")

    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")


main()
