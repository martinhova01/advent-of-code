import time


class Solution:
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = open(self.filename).read().rstrip().split("\n")

    def part1(self):
        nums = [i for i in range(100)]

        i = 50
        s = 0
        for line in self.data:
            dir = line[0]
            num = int(line[1:])
            if dir == "L":
                i = (i - num) % len(nums)
            else:
                i = (i + num) % len(nums)

            if i == 0:
                s += 1

        return s

    def part2(self):
        nums = [i for i in range(100)]

        i = 50
        s = 0
        for line in self.data:
            dir = line[0]
            num = int(line[1:])

            direction = -1 if dir == "L" else 1

            j = num
            while j > 0:

                i = (i + direction) % len(nums)

                if i == 0:
                    s += 1

                j -= 1

        return s


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
