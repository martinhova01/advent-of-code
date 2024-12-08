import time
import itertools

class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = open(self.filename).read().rstrip().split("\n")
        
    def find_antennas(self):
        antennas = {}
        for y, line in enumerate(self.data):
            for x, c in enumerate(line):
                if c == ".":
                    continue
                if c not in antennas:
                    antennas[c] = set()
                antennas[c].add((x, y))
        return antennas
        
    def part1(self):
        antennas = self.find_antennas()
        R = len(self.data)
        C = len(self.data[0])
                
        antinodes = set()
        for _, positions in antennas.items():
            for (x1, y1), (x2, y2) in itertools.product(positions, repeat=2):
                if (x1, y1) == (x2, y2):
                    continue
                
                dx = x2 - x1
                dy = y2 - y1
                
                antinode = (x2 + dx, y2 + dy)
                if antinode[0] < 0 or antinode[0] >= C or antinode[1] < 0 or antinode[1] >= R:
                    continue
                
                antinodes.add(antinode)
        
        return len(antinodes)
    
    
    def part2(self):
        antennas = self.find_antennas()
        R = len(self.data)
        C = len(self.data)
        
        antinodes = set()
        for _, positions in antennas.items():
            for (x1, y1), (x2, y2) in itertools.product(positions, repeat=2):
                if (x1, y1) == (x2, y2):
                    continue
                
                dx = x2 - x1
                dy = y2 - y1
                
                i = -1
                while True:
                    i += 1
                    antinode = (x2 + (dx * i), y2 + (dy * i))
                    if antinode[0] < 0 or antinode[0] >= C or antinode[1] < 0 or antinode[1] >= R:
                        break
                    
                    antinodes.add(antinode)
        
        return len(antinodes)
    
    
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