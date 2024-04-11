import time
from tqdm import tqdm
import re

class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.blueprints = [self.parse_line(line) for line in open(self.filename).read().strip().split("\n")]
        
    def parse_line(self, line: str):
        costs = []
        data = line.split(": ")[1]
        vals = [int(x) for x in re.findall(r"(\d+)", data)]
        costs.append((vals[0], 0, 0)) # ore robot
        costs.append((vals[1], 0, 0)) # clay robot
        costs.append((vals[2], vals[3], 0)) # obsidian robot
        costs.append((vals[4], 0, vals[5])) # geode robot
        return costs
    
    def get_quality(self, blueprint: list[tuple[int, int, int]], limit: int) -> int:
        robots = [1, 0, 0, 0] # ore, clay, obsidian, geode
        mats = [0, 0, 0, 0] # ore, clay, obsidian, geode
        self.memo = {}
        geodes = self.get_max_geodes(blueprint, robots, mats, limit)
        print(geodes)
        return geodes
        
    def get_max_geodes(self, blueprint, robots, mats, remaining_minutes) -> int:
        if remaining_minutes <= 0:
            return mats[3]
        
            #make geode robot if you can afford it
        if mats[0] >= blueprint[3][0] and mats[2] >= blueprint[3][2]:
            new_mats = self.produce(robots, mats)
            new_robots = list(robots)
            new_robots[3] += 1
            new_mats[0] -= blueprint[3][0]
            new_mats[2] -= blueprint[3][2]
            
            
            hashable = (tuple(new_robots), tuple(new_mats), remaining_minutes - 1)
            if hashable not in self.memo:
                self.memo[hashable] = self.get_max_geodes(blueprint, new_robots, new_mats, remaining_minutes - 1)
            return self.memo[hashable]
        
        best = 0
        for i in range(4):
            #make obsidian
            if i == 0:
                if mats[0] >= blueprint[2][0] and mats[1] >= blueprint[2][1] and robots[2] < blueprint[3][2]:
                    new_mats = self.produce(robots, mats)
                    new_robots = list(robots)
                    new_robots[2] += 1
                    new_mats[0] -= blueprint[2][0]
                    new_mats[1] -= blueprint[2][1]
                    
                    hashable = (tuple(new_robots), tuple(new_mats), remaining_minutes - 1)
                    if hashable not in self.memo:
                        self.memo[hashable] = self.get_max_geodes(blueprint, new_robots, new_mats, remaining_minutes - 1)
                    best = max(best, self.memo[hashable])
                
            #make clay
            if i == 1:
                if mats[0] >= blueprint[1][0] and robots[1] < blueprint[2][1]:
                    new_mats = self.produce(robots, mats)
                    new_robots = list(robots)
                    new_robots[1] += 1
                    new_mats[0] -= blueprint[1][0]
                    
                    hashable = (tuple(new_robots), tuple(new_mats), remaining_minutes - 1)
                    if hashable not in self.memo:
                        self.memo[hashable] = self.get_max_geodes(blueprint, new_robots, new_mats, remaining_minutes - 1)
                    best = max(best, self.memo[hashable])
            #make ore
            if i == 2:
                max_cost = max(x[0] for x in blueprint)
                if mats[0] >= blueprint[0][0] and robots[0] < max_cost:
                    new_mats = self.produce(robots, mats)
                    new_robots = list(robots)
                    new_robots[0] += 1
                    new_mats[0] -= blueprint[0][0]
                    
                    hashable = (tuple(new_robots), tuple(new_mats), remaining_minutes - 1)
                    if hashable not in self.memo:
                        self.memo[hashable] = self.get_max_geodes(blueprint, new_robots, new_mats, remaining_minutes - 1)
                    best = max(best, self.memo[hashable])
            #wait
            if i == 3:
                new_mats = self.produce(robots, mats)
                
                hashable = (tuple(robots), tuple(new_mats), remaining_minutes - 1)
                if hashable not in self.memo:
                    self.memo[hashable] = self.get_max_geodes(blueprint, robots, new_mats, remaining_minutes - 1)
                best = max(best, self.memo[hashable])
        
        return best
        
            
    def produce(self, robots, mats):
        new_mats = []
        for i in range(len(robots)):
            new_mats.append(mats[i] + robots[i])
        return new_mats
        
    def part1(self):
        return sum((i+1) * self.get_quality(self.blueprints[i], 24) for i in tqdm(range(len(self.blueprints))))
    
    def part2(self):
        res = 1
        for i in tqdm(range(3)):
            res *= self.get_quality(self.blueprints[i], 32)
        return res
    
    
def main():
    start = time.perf_counter()
    
    s = Solution()
    print("---MAIN---")
    print(f"part 1: {s.part1()}")
    print(f"part 2: {s.part2()}")
    
    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")
    
main()