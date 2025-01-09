import time

class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = open(self.filename).read().rstrip()
        self.parse()
        
    def parse(self):
        self.locks = []
        self.keys = []
        for object in self.data.split("\n\n"):
            object = object.split("\n")
            if object[0][0] == "#":
                #lock
                heights = []
                for x in range(len(object[0])):
                    height = 0
                    while object[height][x] == "#":
                        height += 1
                    heights.append(height)
                self.locks.append(heights)
            else:
                #key
                heights = []
                for x in range(len(object[0])):
                    height = 0
                    y = len(object) - 1
                    while object[y - height][x] == "#":
                        height += 1
                    heights.append(height)
                self.keys.append(heights)
        
    def part1(self):
        s = 0
        max_height = 7
        for lock in self.locks:
            for key in self.keys:
                if any(lock[i] + key[i] > max_height for i in range(len(lock))):
                    continue
                s += 1
        return s
    
    
def main():
    start = time.perf_counter()
    
    s = Solution(test=True)
    print("---TEST---")
    print(f"part 1: {s.part1()}")
    
    s = Solution()
    print("---MAIN---")
    print(f"part 1: {s.part1()}")
    
    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")
    
main()