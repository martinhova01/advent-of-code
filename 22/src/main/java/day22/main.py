import time


class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.graph: list[list[str]] = [line for line in open(self.filename).read().split("\n")][:-2]
        self.path: list[str] = self.getPath()
        self.dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
    def getPath(self):
        pathString = open(self.filename).read().split("\n\n")[1]
        nextIns = ""
        result = []
        for c in pathString:
            if c == "R" or c == "L":
                if nextIns != "":
                    result.append(nextIns)
                    nextIns = ""
                result.append(c)
            else:
                nextIns += c
        result.append(nextIns)
        return result
        
    def findStartX(self):
        return self.graph[0].index(".")
        
    def part1(self):

        x, y = self.findStartX(), 0
        dir = self.dirs[0]
        
        for step in self.path:
            if step == "R":
                dir = self.dirs[(self.dirs.index(dir) + 1) % 4]
            elif step == "L":
                dir = self.dirs[(self.dirs.index(dir) - 1) % 4]
                
            else:
                for _ in range(int(step)):
                    nx, ny = x + dir[0], y + dir[1]
                    if self.isEdge(nx, ny):
                        nx, ny = self.wrap(nx, ny, dir)
                    if self.graph[ny][nx] == "#":
                        break
                    x, y = nx, ny
                    
        return (1000 * (y + 1)) + 4 * (x + 1) + self.dirs.index(dir)
                    
    def isEdge(self, x, y) -> bool:
        if y < 0 or y >= len(self.graph):
            return True
        if x < 0 or x >= len(self.graph[y]):
            return True
        if self.graph[y][x] == " ":
            return True
        return False
        
        
        
    def wrap(self, start_x, start_y, start_dir) -> tuple[int, int]:
        x, y = start_x, start_y
        dir = self.dirs[(self.dirs.index(start_dir) + 2) % 4]
        
        while (x, y) == (start_x, start_y) or not self.isEdge(x, y):
            x, y = x + dir[0], y + dir[1]
            
        return x - dir[0], y - dir[1] # go one tile back
    
    def part2(self):
        return None
    
    
def main():
    start = time.perf_counter()
    # print(len("                                                  ................#..........#...#......##......#..."))
    
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