import time
from collections import Counter, defaultdict, deque
from tqdm import tqdm
import matplotlib.pyplot as plt

def dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def parse(filename):
    lines = open(filename).read().split("\n")
    sensors = []
    beacons = set()
    for line in lines:
        points = line.split("=")
        x = int(points[1].split(",")[0])
        y = int(points[2].split(":")[0])
        beaconX = int(points[3].split(",")[0])
        beaconY = int(points[4])
        sensors.append((x, y, dist(x, y, beaconX, beaconY)))
        beacons.add((beaconX, beaconY))
    return sensors, beacons

class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.sensors = parse(self.filename)[0]
        self.beacons = parse(self.filename)[1]
        
    def part1(self):
        row = 10 if self.test else 2000000
        overlaps = set()
        for sensor in self.sensors:
            ydist = abs(row - sensor[1])
            #no overlap
            if ydist > sensor[2]:
                continue
            x = sensor[0]
            r = sensor[2] - ydist
            overlaps.update(range(x - r, x + r + 1))
            
            
        #remove points where there is a beacon
        counter = 0
        for beacon in self.beacons:
            if beacon[1] == row:
                counter += 1
                
        return len(overlaps) - counter
    
    def part2(self):
        pass
    
    
    def part2Old(self):
        maxValue = 20 if self.test else 4000000
        
        for (x, y, d) in self.sensors:
            x_s = [x, x + d, x, x - d, x]
            y_s = [y - d, y, y + d, y, y - d]
            plt.fill(x_s, y_s)
        plt.plot(
            [0, maxValue, maxValue, 0, 0],
            [0, 0, maxValue, maxValue, 0],
        )
        plt.show()  
        # plt.xlim(left=3403959, right=3403961)
        # plt.ylim(top=3289728, bottom=3289730)
    
    
def main():
    start = time.perf_counter()
    
    s = Solution(test=True)
    print("---TEST---")
    # print(f"part 1: {s.part1()}")
    # print(f"part 2: {s.part2Old()}\n")
    
    s = Solution()
    print("---MAIN---")
    print(f"part 1: {s.part1()}")
    print(f"part 2: {s.part2Old()}")
    
    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")
    
main()