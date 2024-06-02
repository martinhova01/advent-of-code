import time
import re


def is_range_contained(inner: range, outer: range):
    return outer.start <= inner.start and inner.stop <= outer.stop

class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = [self.parse_line(line) for line in open(self.filename).read().split("\n")]
        
    def parse_line(self, line: str):
        instruction, coords = line.split(" ")
        coords = [int(x) for x in re.findall(r"-?\d+", coords)]
        xs, ys, zs = range(coords[0], coords[1] + 1), range(coords[2], coords[3] + 1), range(coords[4], coords[5] + 1)
        return (instruction == "on", xs, ys, zs)
        
    def part1(self):
        grid = [[[False for z in range(-50, 51)] for y in range(-50, 51)] for x in range(-50, 51)]
        for instruction, xs, ys, zs in self.data:
            if not (
                is_range_contained(xs, range(-50, 51))
                and is_range_contained(ys, range(-50, 51))
                and is_range_contained(zs, range(-50, 51))
            ):
                continue
            for x in xs:
                for y in ys:
                    for z in zs:
                        grid[x][y][z] = instruction
                        
        c = 0
        for x in range(-50, 51):
            for y in range(-50, 51):
                for z in range(-50, 51):
                    if grid[x][y][z]:
                        c += 1
        return c
    
    def part2(self):
        pass
    
    
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