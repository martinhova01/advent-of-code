import time
from tqdm import tqdm

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
        self.sensors, self.beacons = parse(self.filename)
        
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
        """The point we are looking for must be one square outside of the edge of one of the sensor-ranges.
        We follow the edge of all the sensor ranges and check each point if it is the correct one.
        """
        maxValue = 20 if self.test else 4000000
        for i in tqdm(range(len(self.sensors))):
            center_x, center_y, d = self.sensors[i]
            #left to top
            x = center_x - (d + 1)
            y = center_y
            while x != center_x or y != center_y - (d + 1):
                if x < 0 or x > maxValue or y < 0 or y > maxValue:
                    break
                if self.checkPoint(x, y, i):
                    print(x, y)
                    return (x * 4000000) + y
                x += 1
                y -= 1
            #top to right
            x = center_x
            y = center_y - (d + 1)
            while x != center_x + (d + 1) or y != center_y:
                if x < 0 or x > maxValue or y < 0 or y > maxValue:
                    break
                if self.checkPoint(x, y, i):
                    print(x, y)
                    return (x * 4000000) + y
                x += 1
                y += 1
            #right to bottom
            x = center_x + (d + 1)
            y = center_y
            while x != center_x or y != center_y + (d + 1):
                if x < 0 or x > maxValue or y < 0 or y > maxValue:
                    break
                if self.checkPoint(x, y, i):
                    print(x, y)
                    return (x * 4000000) + y
                x -= 1
                y += 1
            #bottom to left
            x = center_x
            y = center_y + (d + 1)
            while x != center_x - (d + 1) or y != center_y:
                if x < 0 or x > maxValue or y < 0 or y > maxValue:
                    break
                if self.checkPoint(x, y, i):
                    print(x, y)
                    return (x * 4000000) + y
                x -= 1
                y -= 1
    
    
    def checkPoint(self, x: int, y: int, sensor_nr: int):
        """A point is the correct point if it is outside the range of all other sensors.

        Args:
            x (int): x to check
            y (int): y to check
            sensor (int): index of sensor to not check

        Returns:
            boolean: True if this is the correct point
        """
        c = 0
        for i in range(len(self.sensors)):
            center_x, center_y, d = self.sensors[i]
            if i == sensor_nr:
                continue
            if dist(x, y, center_x, center_y) > d:
                c += 1
        return c == len(self.sensors) - 1
    
    
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