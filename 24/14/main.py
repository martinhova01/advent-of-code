import time
from collections import defaultdict
import re

class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = open(self.filename).read().rstrip()
        self.C = 11 if self.test else 101
        self.R = 7 if self.test else 103
        
    def part1(self):
        robots = defaultdict(int)
        for line in self.data.split("\n"):
            nums = [int(x) for x in re.findall(r"-?\d+", line)]
            start_x, start_y = nums[0], nums[1]
            v_x, v_y = nums[2], nums[3]
            x, y = (start_x + v_x * 100) % self.C, (start_y + v_y * 100) % self.R
            robots[(x, y)] += 1
            
        
        q1 = 0
        for x in range(self.C // 2):
            for y in range(self.R // 2):
                if (x, y) in robots:
                    q1 += robots[(x, y)]
        q2 = 0
        for x in range(self.C // 2 + 1, self.C):
            for y in range(self.R // 2):
                if (x, y) in robots:
                    q2 += robots[(x, y)]
                    
        q3 = 0
        for x in range(self.C // 2):
            for y in range(self.R // 2 + 1, self.R):
                if (x, y) in robots:
                    q3 += robots[(x, y)]
        
        q4 = 0
        for x in range(self.C // 2 + 1, self.C):
            for y in range(self.R // 2 + 1, self.R):
                if (x, y) in robots:
                    q4 += robots[(x, y)]
                    
        return q1*q2*q3*q4
    
    
    def move(self, robots):
        new_robots = defaultdict(list)
        for (x, y), vels in robots.items():
            for dx, dy in vels:   
                new_robots[((x + dx) % self.C, (y + dy) % self.R)].append((dx, dy))
        
        return new_robots


    def print_robots(self, robots):
        s = ""
        for x in range(self.C):
            for y in range(self.R):
                if (x, y) in robots.keys():
                    s += "#"
                else:
                    s += " "
            s += "\n"
        with open("out.txt", "w") as f:
            f.write(s)
            
            
    def score(self, robots: dict):
        score = 0
        for y in range(self.R):
            s = 0
            for x in range(self.C):
                if (x, y) in robots.keys():
                    s += 1
            score = max(score, s)
        return score
                
    
    def part2(self):
        robots = defaultdict(list)
        for line in self.data.split("\n"):
            nums = [int(x) for x in re.findall(r"-?\d+", line)]
            start_x, start_y = nums[0], nums[1]
            v_x, v_y = nums[2], nums[3]
            robots[(start_x, start_y)].append((v_x, v_y))
            
            
        best = 0
        best_i = 0
        for i in range(1, 10_000):
            robots = self.move(robots)
            score = self.score(robots)
            #uncomment to print the result
            # if i == 6446:
            #     self.print_robots(robots)
            #     break
            if score > best:
                best = score
                best_i = i
        return best_i
    
    
def main():
    start = time.perf_counter()
    
    s = Solution(test=True)
    print("---TEST---")
    print(f"part 1: {s.part1()}")
    # print(f"part 2: {s.part2()}\n")
    
    s = Solution()
    print("---MAIN---")
    print(f"part 1: {s.part1()}")
    print(f"part 2: {s.part2()}")
    
    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")
    
main()