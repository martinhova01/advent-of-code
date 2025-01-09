import time
from functools import cache

class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = open(self.filename).read().rstrip().split("\n")
        self.numbers = {
            "7": (0, 0),
            "8": (1, 0),
            "9": (2, 0),
            "4": (0, 1),
            "5": (1, 1),
            "6": (2, 1),
            "1": (0, 2),
            "2": (1, 2),
            "3": (2, 2),
            "0": (1, 3),
            "A": (2, 3)
        }
        self.directions = {
            "^": (1, 0),
            "A": (2, 0),
            "<": (0, 1),
            "v": (1, 1),
            ">": (2, 1)
        }
        self.memo = {}
    
    @cache
    def shortest_sequence(self, sequence: str, steps):
        if steps == 0:
            return len(sequence)
        
        s = 0   
        if sequence[:-1].isnumeric():
            x, y = 2, 3
            for c in sequence:
                goal = self.numbers[c]
                dx, dy = goal[0] - x, goal[1] - y
                addition_x = ""
                if dx < 0:
                    addition_x = "<" * abs(dx)
                else:
                    addition_x = ">" * dx
                
                addition_y = ""
                if dy < 0:
                    addition_y = "^" * abs(dy)
                else:
                    addition_y = "v" * dy
                    
                new_sequences = set()
                if x == 0 and goal[1] == 3:
                    new_sequences.add(addition_x + addition_y + "A")
                
                elif y == 3 and goal[0] == 0:
                    new_sequences.add(addition_y + addition_x + "A")
                
                else:
                    new_sequences.add(addition_x + addition_y + "A")
                    new_sequences.add(addition_y + addition_x + "A")
                
                best = float("inf")
                for seq in new_sequences:
                    best = min(best, self.shortest_sequence(seq, steps - 1))
                x, y = goal
                s += best
                
        else:
            x, y = 2, 0
            for c in sequence:
                goal = self.directions[c]
                dx, dy = goal[0] - x, goal[1] - y
                addition_x = ""
                if dx < 0:
                    addition_x = "<" * abs(dx)
                else:
                    addition_x = ">" * dx
                
                addition_y = ""
                if dy < 0:
                    addition_y = "^" * abs(dy)
                else:
                    addition_y = "v" * dy
                    
                new_sequences = set()   
                if x == 0 and y == 1:
                    new_sequences.add(addition_x + addition_y + "A")
                
                elif y == 0 and goal[0] == 0:
                    new_sequences.add(addition_y + addition_x + "A")
                
                else:
                    new_sequences.add(addition_x + addition_y + "A")
                    new_sequences.add(addition_y + addition_x + "A")
                    
                best = float("inf")
                for seq in new_sequences:
                    best = min(best, self.shortest_sequence(seq, steps - 1))
                x, y = goal
                s += best
                
        return s
            
            
            
            
        
        
                
    def part1(self):
        return sum(self.shortest_sequence(num, 3) * int(num[:-1]) for num in self.data)

    
    def part2(self):
        return sum(self.shortest_sequence(num, 26) * int(num[:-1]) for num in self.data)
    
    
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