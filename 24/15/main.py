import time

class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = open(self.filename).read().rstrip().split("\n\n")
        self.directions = {"^": (0, -1), ">": (1, 0), "v": (0, 1), "<": (-1, 0)}
        
    def part1(self):
        grid, moves = self.data
        grid = [list(line) for line in grid.split("\n")]
        moves = moves.replace("\n", "")
        
        R = len(grid)
        C = len(grid[0])
        start_x, start_y = 0, 0
        for x in range(C):
            for y in range(R):
                if grid[y][x] == "@":
                    start_x, start_y = x, y
                    
        x, y = start_x, start_y
        for move in moves:
            dx, dy = self.directions[move]
            _nx, ny = x + dx, y + dy
            if grid[ny][_nx] == "#":
                continue
            if grid[ny][_nx] == "O":
                # check if stone can move
                i = 1
                while grid[y + dy * i][x + dx *i] == "O":
                    i += 1
                if grid[y + dy * i][x + dx *i] == ".":
                    # move stones
                    for k in range(i, 0, -1):
                        grid[y + dy * k][x + dx * k] = grid[y + dy * (k - 1)][x + dx * (k - 1)]
                    grid[y][x] = "."
                    x, y = _nx, ny
                else:
                    continue
            else:
                assert grid[ny][_nx] == "."
                grid[y][x] = "."
                grid[ny][_nx] = "@"
                x, y = _nx, ny
            
        s = 0
        for y in range(R):
            for x in range(C):
                if grid[y][x] == "O":
                    s += 100 * y + x
        return s
            
    
    def part2(self):
        grid, moves = self.data
        grid = [list(line) for line in grid.split("\n")]
        moves = moves.replace("\n", "")
        
        R = len(grid)
        C = len(grid[0])
        
        # double the width
        new_grid = []
        for y in range(R):
            new_line = []
            for x in range(C):
                c = grid[y][x]
                if c == "#":
                    new_line.extend(["#", "#"])
                elif c == "O":
                    new_line.extend(["[", "]"])
                elif c == ".":
                    new_line.extend([".", "."])
                elif c == "@":
                    new_line.extend(["@", "."])
            new_grid.append(new_line)
        
        grid = new_grid
        R = len(grid)
        C = len(grid[0])
        start_x, start_y = 0, 0
        for x in range(C):
            for y in range(R):
                if grid[y][x] == "@":
                    start_x, start_y = x, y
                    
        x, y = start_x, start_y
        for move in moves:
            dx, dy = self.directions[move]
            _nx, ny = x + dx, y + dy
            if grid[ny][_nx] == "#":
                #hit wall
                continue
            if grid[ny][_nx] == "[" or grid[ny][_nx] == "]":
                # check if stone can move
                if move == ">" or move == "<":
                    #left or right
                    i = 1
                    while grid[y + dy * i][x + dx *i] == "[" or grid[y + dy * i][x + dx *i] == "]":
                        i += 1
                    if grid[y + dy * i][x + dx *i] == ".":
                        # move stones
                        for k in range(i, 0, -1):
                            grid[y + dy * k][x + dx * k] = grid[y + dy * (k - 1)][x + dx * (k - 1)]
                        grid[y][x] = "."
                        x, y = _nx, ny
                    else:
                        continue
                else:
                    #up or down
                    offsets = {} # offsets in x direction containing stones
                    offsets[0] = set()
                    offsets[0].add(0)
                    i = 0
                    can_move = None
                    while True:
                        i += 1
                        
                        if any(grid[y + dy * i][x + offset_x] == "#" for offset_x in offsets[i - 1]):
                            # one of the stones hit a stone, stop
                            can_move = False
                            break
                        
                        if not any(grid[y + dy * i][x + offset_x] in "[]" for offset_x in offsets[i - 1]):
                            # free space, can move
                            can_move = True
                            break
                        
                        offsets[i] = set()
                        for offset_x in offsets[i - 1]:
                            if grid[y + dy * i][x + offset_x] == "[":
                                offsets[i].add(offset_x)
                                offsets[i].add(offset_x + 1)
                            elif grid[y + dy * i][x + offset_x] == "]":
                                offsets[i].add(offset_x)
                                offsets[i].add(offset_x - 1)
                                
                    if can_move:
                        # move all stones
                        for k in range(i, 0, -1):
                            for offset_x in offsets[k - 1]:  
                                grid[y + dy * k][x + offset_x] = grid[y + dy * (k - 1)][x + offset_x]
                                grid[y + dy * (k - 1)][x + offset_x] = "."
                        x, y = _nx, ny
                    
                    
            else:
                # move into empty space
                assert grid[ny][_nx] == "."
                grid[y][x] = "."
                grid[ny][_nx] = "@"
                x, y = _nx, ny
        
        s = 0
        for y in range(R):
            for x in range(C):
                if grid[y][x] == "[":
                    s += 100 * y + x
        return s
    
    
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