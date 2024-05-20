import time
from functools import reduce


class Packet():
    def __init__(self, data: str):
        self.version: int = int(data[:3], 2)
        self.type: int = int(data[3:6], 2)
        self.children: list[Packet] = []
        self.literal: int = None
        self.length: int = 6
        
        if self.type == 4:
            self.literal = self.parse_literal(data[6:])
        else:
            length_type = data[6]
            if length_type == "0":
                self.length += 16
                payload_length = int(data[7:22], 2)
                self.children = self.parse_packets_by_length(data[22:], payload_length)
                
            else:
                self.length += 12
                number_of_packets = int(data[7:18], 2)
                self.children = self.parse_packets_by_number(data[18:], number_of_packets)
            
            self.length += sum(x.length for x in self.children)
         
         
    def evaluate(self):
        
        if self.type == 0:
            return sum(x.evaluate() for x in self.children)
        
        elif self.type == 1:
            return reduce(lambda x, y : x * y, [p.evaluate() for p in self.children])
        
        elif self.type == 2:
            return min(x.evaluate() for x in self.children)
        
        elif self.type == 3:
            return max(x.evaluate() for x in self.children)
        
        if self.type == 4:
            return self.literal
        
        elif self.type == 5:
            p1, p2 = self.children
            return 1 if p1.evaluate() > p2.evaluate() else 0
            
        elif self.type == 6:
            p1, p2 = self.children
            return 1 if p1.evaluate() < p2.evaluate() else 0
            
        elif self.type == 7:
            p1, p2 = self.children
            return 1 if p1.evaluate() == p2.evaluate() else 0
        
    def parse_literal(self, payload: str):
        res = ""
        for i in range(0, len(payload), 5):
            res += payload[i + 1 : i + 5]
            if payload[i] == "0":
                break
        self.length += i + 5
        return int(res, 2)
    
    def parse_packets_by_length(self, payload: str, length: int):
        res = []
        l = 0
        while l < length:
            p = Packet(payload[l:])
            res.append(p)
            l += p.length
        return res
        
    
    def parse_packets_by_number(self, payload: str, number: int):
        res = []
        l = 0
        for _ in range(number):
            p = Packet(payload[l:])
            res.append(p)
            l += p.length
        return res
            
        

class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = bin(int(open(self.filename).read(), 16))[2:]
        
        #add leading 0s 
        while len(self.data) % 4 != 0:
            self.data = "0" + self.data
        
    def part1(self):
        root = Packet(self.data)
        res = 0
        q = [root]
        while q:
            u = q.pop()
            res += u.version
            for v in u.children:
                q.append(v)
        return res
            
    
    def part2(self):
        return Packet(self.data).evaluate()
    
    
def main():
    start = time.perf_counter()
    
    # s = Solution(test=True)
    # print("---TEST---")
    # print(f"part 1: {s.part1()}")
    # print(f"part 2: {s.part2()}\n")
    
    s = Solution()
    print("---MAIN---")
    print(f"part 1: {s.part1()}")
    print(f"part 2: {s.part2()}")
    
    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")
    
main()