import time


class Solution:
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = open(self.filename).read().rstrip().split("\n")

    def part1(self):
        res = 0
        for line in self.data:
            nums = list(map(int, line))
            best = 0
            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):

                    n = int(str(nums[i]) + str(nums[j]))
                    best = max(best, n)
            res += best

        return res

    def find_largest(self, nums, length):
        if length == 0:
            return ""

        best = 0
        best_i = -1
        for i in range(len(nums)):
            if len(nums) - i + 1 <= length:
                break
            if nums[i] > best:
                best = nums[i]
                best_i = i

        return str(best) + self.find_largest(nums[best_i + 1 :], length - 1)

    def part2(self):
        res = 0
        for line in self.data:
            nums = list(map(int, line))
            res += int(self.find_largest(tuple(nums), 12))

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
