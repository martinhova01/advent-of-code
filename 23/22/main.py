import time
from collections import deque


class Brick:
    def __init__(self, corner1, corner2):
        self.supports = set()
        self.supporters = set()
        self.squares = []
        for x in range(min(corner1[0], corner2[0]), max(corner1[0], corner2[0]) + 1):
            for y in range(min(corner1[1], corner2[1]), max(corner1[1], corner2[1]) + 1):
                for z in range(min(corner1[2], corner2[2]), max(corner1[2], corner2[2]) + 1):
                    self.squares.append((x, y, z))
                    
    def get_lowest_z(self):
        m = float("inf")
        for s in self.squares:
            if s[2] < m:
                m = s[2]
        return m
    
    def move_down(self):
        for i in range(len(self.squares)):
            s = self.squares[i]
            self.squares[i] = (s[0], s[1], s[2] - 1)
    

class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.bricks = self.parse()
        self.cannot_disintegrate = set()
        
    def parse(self):
        bricks = []
        for line in open(self.filename).read().split("\n"):
            corner1 = eval(f"({line.split("~")[0]})")
            corner2 = eval(f"({line.split("~")[1]})")
            bricks.append(Brick(corner1, corner2))
        return bricks
    
    def settle_bricks(self):
        self.bricks = sorted(self.bricks, key=lambda b: b.get_lowest_z())
        
        changed = True
        while changed:
            changed = False
            for brick in self.bricks:
                if self.can_move_down(brick):
                    brick.move_down()
                    changed = True
        
                    
    def can_move_down(self, brick) -> bool:
        if brick.get_lowest_z() == 1:
            return False
        for (x, y, z) in brick.squares:
            if (x, y, z - 1) in brick.squares:
                continue
            
            for b in self.bricks:
                if b == brick:
                    continue
                if (x, y, z - 1) in b.squares:
                    return False
        return True
    
    def create_graph(self):
        self.settle_bricks()
        
        for brick in self.bricks:
            for (x, y, z) in brick.squares:
                if (x, y, z - 1) in brick.squares:
                    continue
                for b in self.bricks:
                    if b == brick:
                        continue
                    if (x, y, z - 1) in b.squares:
                        brick.supporters.add(b)
                        b.supports.add(brick)
        
    def part1(self):
        self.create_graph()
        cannot_disintegrate = set()
        for brick in self.bricks:
            if len(brick.supporters) == 1:
                cannot_disintegrate.update(brick.supporters)
                
        self.cannot_disintegrate = cannot_disintegrate
                
        return len(set(self.bricks).difference(cannot_disintegrate))
    
    def bfs(self, start):
        q = deque()
        q.append(start)
        removed = set()
        removed.add(start)
        while q:
            current = q.popleft()
            if all(supp in removed for supp in current.supporters):
                removed.add(current)
            for b in current.supports:
                q.append(b)
        return removed
        
    
    def part2(self):
        res = 0
        for brick in self.cannot_disintegrate:
            removed = self.bfs(brick)
            res += len(removed) - 1
        return res
    
    
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