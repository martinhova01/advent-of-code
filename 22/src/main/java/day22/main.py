import time

def rotate_point_x(point: tuple[float, float, float], positive_dir: bool) -> tuple[float, float, float]:
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

def rotate_point_y(point: tuple[float, float, float], positive_dir: bool) -> tuple[float, float, float]:
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
    """The front face has z = 25.5
        the back face has z = -25.5
        the top face has y = -25.5
        the bottom face has y = 25.5
        the left face has x = -25.5
        the right face has x = 25.5
    """
    def __init__(self, filename):
        self.filename = filename
        self.walls: set[tuple[float, float, float]] = self.parse_cube()
        
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
        
    def parse_cube(self) -> set[tuple[float, float, float]]:
        walls = set()
        lines = open(self.filename).read().split("\n")[:-2]
        
        z = 25.5
        #top
        top_face = set()
        for x in range(50, 100):
            for y in range(50):
                if lines[y][x] == "#":
                    top_face.add((x - 50 - 24.5, y - 24.5, z))
        
        for point in top_face:
            walls.add(rotate_point_x(point, True))
        
            
        #right
        right_face = set()
        for x in range(100, 150):
            for y in range(50):
                if lines[y][x] == "#":
                    right_face.add((x - 100 - 24.5, y - 24.5, z))
                    
        for point in right_face:
            walls.add(rotate_point_x(rotate_point_y(point, True), True))
            
        #front
        front_face = set()
        for x in range(50, 100):
            for y in range(50, 100):
                if lines[y][x] == "#":
                    front_face.add((x - 50 - 24.5, y - 50 - 24.5, z))
        
        for point in front_face:
            walls.add(point)
            
        #bottom
        bottom_face = set()
        for x in range(50, 100):
            for y in range(100, 150):
                if lines[y][x] == "#":
                    bottom_face.add((x - 50 - 24.5, y - 100 - 24.5, z))
        
        for point in bottom_face:
            walls.add(rotate_point_x(point, False))
            
        #left
        left_face = set()
        for x in range(50):
            for y in range(100, 150):
                if lines[y][x] == "#":
                    left_face.add((x - 24.5, y - 100 - 24.5, z))
                    
        for point in left_face:
            walls.add(rotate_point_x(rotate_point_y(point, False), False))
            
        #back
        back_face = set()
        for x in range(50):
            for y in range(150, 200):
                if lines[y][x] == "#":
                    back_face.add((x - 24.5, y - 150 - 24.5, z))
                    
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
        cube.rotate_x(False) # start position is on the top-face
        x, y, z = -24.5, -24.5, 25.5
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
                    
                    if nx <= -25.5:
                        cube.rotate_y(True)
                        nx = 24.5
                        if (nx, ny, z) in cube.walls:
                            cube.rotate_y(False) #undo rotate
                            break
                        rotations.append(("y", True))
                        
                    if nx >= 25.5:
                        cube.rotate_y(False)
                        nx = -24.5
                        if (nx, ny, z) in cube.walls:
                            cube.rotate_y(True) #undo rotate
                            break
                        rotations.append(("y", False))
                        
                    if ny <= -25.5:
                        cube.rotate_x(False)
                        ny = 24.5
                        if (nx, ny, z) in cube.walls:
                            cube.rotate_x(True) #undo rotate
                            break
                        rotations.append(("x", False))
                        
                    if ny >= 25.5:
                        cube.rotate_x(True)
                        ny = -24.5
                        if (nx, ny, z) in cube.walls:
                            cube.rotate_x(False) #undo rotate
                            break
                        rotations.append(("x", True))
                        
                    if (nx, ny, z) in cube.walls:
                        break
                    
                    x, y = nx, ny
                    
                    
        dir = (dir[0], dir[1], 0)
        
            #do the rotations backwards to find out what face the final position is on
        for i in range(len(rotations) - 1, -1, -1):
            rotation = rotations[i]
            if rotation[0] == "x":
                x, y, z = rotate_point_x((x, y, z), not rotation[1])
                dir = rotate_point_x(dir, not rotation[1])
            else:
                x, y, z = rotate_point_y((x, y, z), not rotation[1])
                dir = rotate_point_y(dir, not rotation[1])
                
        
            #unfold left-face to map rotation
            #change these based on what face the final position is on
        x, y, z = rotate_point_y(rotate_point_x((x, y, z), True), True)
        dir = rotate_point_y(rotate_point_x(dir, True), True)
        
        
            #find the row- and colnumber based on what face the final position is on
            #change these based on what face the final position is on
        row = int(y + 100 + 24.5 + 1)
        col = int(x + 0 + 24.5 + 1)
        
        dir = dirs.index((dir[0], dir[1]))
        
        return 1000 * row + 4 * col + dir
        
        
        
        
    
    
def main():
    start = time.perf_counter()
    
    s = Solution(test=True)
    print("---TEST---")
    print(f"part 1: {s.part1()}")
    
    s = Solution()
    print("---MAIN---")
    print(f"part 1: {s.part1()}")
    print(f"part 2: {s.part2()}")
    
    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")
    
    
main()