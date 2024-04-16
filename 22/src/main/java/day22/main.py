import time


def rotate_point_x(point: tuple[int, int, int], positive_dir: bool) -> tuple[int, int, int]:
    """Rotate a point along the x-axis.

    Args:
        point tuple[int, int, int]: the original point
        positive_dir (bool): True if rotation is along positive direction

    Returns:
        tuple[int, int, int]: the rotated point
    """
    if positive_dir:
        return (point[0], -point[2], point[1])
    else:
        return (point[0], point[2], -point[1])

def rotate_point_y(point: tuple[int, int, int], positive_dir: bool) -> tuple[int, int, int]:
    """Rotate a point along the y-axis.

    Args:
        point tuple[int, int, int]: the original point
        positive_dir (bool): True if rotation is along positive direction

    Returns:
        tuple[int, int, int]: the rotated point
    """
    if positive_dir:
        return (point[2], point[1], -point[0])
    else:
        return (-point[2], point[1], point[0])
        

class Cube():
    """The front face has z = 25
        the back face has z = -25
        the top face has y = -25
        the bottom face has y = 25
        the left face has x = -25
        the right face has x = 25
    """
    def __init__(self, filename):
        self.filename = filename
        self.walls: set[tuple[int, int, int]] = self.parse_cube()
        
    def rotate_x(self, positive_dir: bool):
        new_walls = set()
        for wall in self.walls:
            new_walls.add(rotate_point_x(wall, positive_dir))
        self.walls = new_walls
            
    def rotate_y(self, positive_dir: bool):
        new_walls = set()
        for wall in self.walls:
            new_walls.add(rotate_point_y(wall, positive_dir))
        self.walls = new_walls
        
    def parse_cube(self) -> set[tuple[int, int, int]]:
        walls = set()
        lines = open(self.filename).read().split("\n")[:-2]
        
        z = 25
        #top
        top_face = set()
        for x in range(50, 100):
            for y in range(50):
                if lines[y][x] == "#":
                    top_face.add((x - 50 - 25, y - 25, z))
        
        for point in top_face:
            walls.add(rotate_point_x(point, True))
        
            
        #right
        right_face = set()
        for x in range(100, 150):
            for y in range(50):
                if lines[y][x] == "#":
                    right_face.add((x - 100 - 25, y - 25, z))
                    
        for point in right_face:
            walls.add(rotate_point_x(rotate_point_y(point, True), True))
            
        #front
        front_face = set()
        for x in range(50, 100):
            for y in range(50, 100):
                if lines[y][x] == "#":
                    front_face.add((x - 50 - 25, y - 50 - 25, z))
        
        for point in front_face:
            walls.add(point)
            
        #bottom
        bottom_face = set()
        for x in range(50, 100):
            for y in range(100, 150):
                if lines[y][x] == "#":
                    bottom_face.add((x - 50 - 25, y - 100 - 25, z))
        
        for point in bottom_face:
            walls.add(rotate_point_x(point, False))
            
        #left
        left_face = set()
        for x in range(50):
            for y in range(100, 150):
                if lines[y][x] == "#":
                    left_face.add((x - 25, y - 100 - 25, z))
                    
        for point in left_face:
            walls.add(rotate_point_x(rotate_point_y(point, False), False))
            
        #back
        back_face = set()
        for x in range(50):
            for y in range(150, 200):
                if lines[y][x] == "#":
                    back_face.add((x - 25, y - 150 - 25, z))
                    
        for point in back_face:
            walls.add(rotate_point_y(rotate_point_x(rotate_point_y(point, False), False), False))
        
        return walls
            
        
        


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
        cube = Cube(self.filename)
        
        rotations = [("x", False)]
        cube.rotate_x(False)
        x, y, z = -25, -25, 25
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        dir = dirs[0]
        
        for step in self.path:
            if step == "R":
                dir = dirs[(dirs.index(dir) + 1) % 4]
            elif step == "L":
                dir = dirs[(dirs.index(dir) - 1) % 4]
                
            else:
                for _ in range(int(step)):
                    nx, ny = x + dir[0], y + dir[1]
                    
                    if nx == -26:
                        cube.rotate_y(True)
                        nx = 25
                        if (nx, ny, z) in cube.walls:
                            cube.rotate_y(False) #undo rotate
                            break
                        rotations.append(("y", True))
                        
                    if nx == 26:
                        cube.rotate_y(False)
                        nx = -25
                        if (nx, ny, z) in cube.walls:
                            cube.rotate_y(True)
                            break
                        rotations.append(("y", False))
                        
                    if ny == -26:
                        cube.rotate_x(False)
                        ny = 25
                        if (nx, ny, z) in cube.walls:
                            cube.rotate_x(True)
                            break
                        rotations.append(("x", False))
                        
                    if ny == 26:
                        cube.rotate_x(True)
                        ny = -25
                        if (nx, ny, z) in cube.walls:
                            cube.rotate_x(False)
                            break
                        rotations.append(("x", True))
                        
                    if (nx, ny, z) in cube.walls:
                        break
                    
                    x, y = nx, ny
                    
        dir = (dir[0], dir[1], 0)
        print(x, y, z, dir)
        
            #do the rotations backwards to find out what face the final position is on
        for i in range(len(rotations) - 1, -1, -1):
            rotation = rotations[i]
            if rotation[0] == "x":
                x, y, z = rotate_point_x((x, y, z), not rotation[1])
                dir = rotate_point_x(dir, not rotation[1])
            else:
                x, y, z = rotate_point_y((x, y, z), not rotation[1])
                dir = rotate_point_y(dir, not rotation[1])
                
        print(x, y, z, dir)
        
            #change these based on what face the final position is on
        x, y, z = rotate_point_y(rotate_point_x(rotate_point_y((x, y, z), True), True), True) # unfold back-face to map rotation
        dir = rotate_point_y(rotate_point_x(rotate_point_y(dir, True), True), True)
        
        print(x, y, z, dir)
        
            #change these based on what face the final position is on
        row = y + 150 + 25 + 1
        col = x + 25 + 1
        
        dir = dirs.index((dir[0], dir[1]))
        
        return 1000 * row + 4 * col + dir
        
        
        
        
    
    
def main():
    start = time.perf_counter()
    
    s = Solution(test=True)
    print("---TEST---")
    print(f"part 1: {s.part1()}")
    # print(f"part 2: {s.part2()}\n")
    
    s = Solution()
    print("---MAIN---")
    print(f"part 1: {s.part1()}")
    print(f"part 2: {s.part2()}") # 15591 too low / 143203 too high / 143200 not right answer
    
    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")
    
    # x, y, z = 25, 0, -25
    # print(rotate_point_y((x, y, z), False))
    
    
main()