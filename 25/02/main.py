import time


class Solution:
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = open(self.filename).read().rstrip().split(",")

    def part1(self):
        res = 0
        for line in self.data:
            start, stop = list(map(int, line.split("-")))
            for i in range(start, stop + 1):
                s = str(i)
                if s[: len(s) // 2] == s[len(s) // 2 :]:
                    res += int(s)

        return res

    def part2(self):
        res = 0
        for line in self.data:
            start, stop = list(map(int, line.split("-")))
            for i in range(start, stop + 1):
                s = str(i)

                for length in range(1, (len(s) // 2 + 1)):
                    if len(s) % length != 0:
                        continue
                    parts = len(s) // length
                    if all(
                        s[length * (i - 1) : length * i]
                        == s[length * i : length * (i + 1)]
                        for i in range(1, parts)
                    ):
                        res += int(s)
                        break

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
