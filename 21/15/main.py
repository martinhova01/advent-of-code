import heapq
import copy

class Solution:
    def __init__(self, test) -> None:
        self.filename = "testinput.txt" if test else "input.txt" 
        self.data = [[int(x) for x in line] for line in open(self.filename).read().split("\n")]
        self.directions = {(1, 0), (0, 1), (-1, 0), (0, -1)}
        
    def part1(self) -> int:
        return self.findShortestPath(self.data)
    
    def part2(self) -> int:
        riskLevels = copy.deepcopy(self.data)
            #adding copies down
        for _ in range(4):
            riskLevels = riskLevels + copy.deepcopy(self.data)
            
        for i in range(len(self.data), len(riskLevels)):
            for j in range(len(riskLevels[i])):
                uppValue = riskLevels[i - len(self.data)][j]
                riskLevels[i][j] = 1 if uppValue + 1 > 9 else uppValue + 1
                           
            #adding copies right
        for i in range(len(riskLevels)):
            for x in range(len(riskLevels[i]), len(riskLevels[i] * 5)):
                    leftValue = riskLevels[i][x - len(self.data)]
                    riskLevels[i].append(1 if leftValue + 1 > 9 else leftValue + 1)
                           
        return self.findShortestPath(riskLevels)

    
        #finds shortest path using dijkstras algorithm
    def findShortestPath(self, riskLevels):
        points = [[Point(i, j, float('inf')) for i in range(len(riskLevels[j]))] for j in range(len(riskLevels))]
        points[0][0].d = 0
        endPoint = (len(points) - 1, len(points[0]) - 1)
        Q = []
        for i in range(len(riskLevels)):
            for j in range(len(riskLevels[i])):
                heapq.heappush(Q, points[i][j])
        
        while Q:
            u: Point = heapq.heappop(Q)
            for (dx, dy) in self.directions:
                x = u.x + dx
                y = u.y + dy
                    #check out of bounds
                if x < 0 or x >= len(points[0]) or y < 0 or y >= len(points):
                    continue
                v: Point = points[y][x]
                if self.relax(u, v, riskLevels):
                    heapq.heappush(Q, v)
                    if (x, y) == endPoint:
                        return v.d
        
        #return True if best distance changed
    def relax(self, u, v, riskLevels):
        if v.d > u.d + riskLevels[v.y][v.x]:
            v.d = u.d + riskLevels[v.y][v.x]
            return True
        return False
            
class Point:
    def __init__(self, x, y, d) -> None:
        self.x = x
        self.y = y
        self.d = d
        
        #makes it possible to compare two Point objects
    def __lt__(self, other):
        return self.d < other.d

def main(test = False):
    s = Solution(test)
    print(f"part1: {s.part1()}")
    print(f"part2: {s.part2()}")
    
main()