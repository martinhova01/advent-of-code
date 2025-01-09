import time
from collections import deque

class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = open(self.filename).read().rstrip()
        self.parse()
    
    def parse(self):
        self.values = {}
        values, gates = self.data.split("\n\n")
        for line in values.split("\n"):
            key, value = line.split(": ")
            self.values[key] = int(value)
        
        self.operations = []
        for line in gates.split("\n"):
            x, op, y, _, z = line.split(" ")
            self.operations.append((x, op, y, z))
            
            
    def run(self, operations):
        q = deque(operations)
        while q:
            x, op, y, z = q.popleft()
            if x not in self.values or y not in self.values:
                q.append((x, op, y, z))
                continue
                
            if op == "AND": 
                self.values[z] = self.values[x] & self.values[y]
            elif op == "OR":
                self.values[z] = self.values[x] | self.values[y]
            else:
                self.values[z] = self.values[x] ^ self.values[y]
        
        filtered = sorted((filter(lambda x : x.startswith("z"), self.values)), reverse=True)
        binary = "".join(str(self.values[x]) for x in filtered)
        return int(binary, 2)
    
        
    def part1(self):
        return self.run(self.operations)
            
    
    def part2(self):
        """
        I realised that the gates follow the standard format of adders(see adder.png).
        I created a loop that checks if the gates follow the correct format, if not an error is thrown.
        Based on where the error occured, I manually found which two wires to swap.
        """
        operations = list(self.operations)
        s1 = operations.index(("vsb", "AND", "dkp", "z38"))
        s2 = operations.index(("dkp", "XOR", "vsb", "hqh"))
        operations[s1], operations[s2] = (*operations[s1][:-1], operations[s2][-1]), (*operations[s2][:-1], operations[s1][-1])
        
        s3 = operations.index(("x28", "XOR", "y28", "qdq"))
        s4 = operations.index(("y28", "AND", "x28", "pvb"))
        operations[s3], operations[s4] = (*operations[s3][:-1], operations[s4][-1]), (*operations[s4][:-1], operations[s3][-1])
        
        s5 = operations.index(("pwp", "OR", "cwc", "z24"))
        s6 = operations.index(("qvs", "XOR", "kmc", "mmk"))
        operations[s5], operations[s6] = (*operations[s5][:-1], operations[s6][-1]), (*operations[s6][:-1], operations[s5][-1])
        
        s7 = operations.index(("sbs", "XOR", "vbj", "vkq"))
        s8 = operations.index(("x11", "AND", "y11", "z11"))
        operations[s7], operations[s8] = (*operations[s7][:-1], operations[s8][-1]), (*operations[s8][:-1], operations[s7][-1])
        
        gates = {}
        for x, op, y, z in operations:
            gates[z] = (x, op, y)
            
        c_out = "z45"
        for i in range(44, 0, -1):
            #uncomment line below to see where the error is
            # print(i, c_out)
            _or = gates[c_out]
            assert _or[1] == "OR"
            
            and1 = gates[_or[0]]
            assert and1[1] == "AND"
            
            and2 = gates[_or[2]]
            assert and2[1] == "AND"
            
            x = f"x{i:02d}"
            y = f"y{i:02d}"
            
            assert and1 == (x, "AND", y) or and1 == (y, "AND", x) or and2 == (x, "AND", y) or and2 == (y, "AND", x)
            
            z = f"z{i:02d}"
            xor1 = gates[z]
            assert xor1[1] == "XOR"
            
            if gates[xor1[0]] == (x, "XOR", y) or gates[xor1[0]] == (y, "XOR", x):
                c_in = xor1[2]
            elif gates[xor1[2]] == (x, "XOR", y) or gates[xor1[2]] == (y, "XOR", x):
                c_in = xor1[0]
            else:
                assert False
                
            c_out = c_in
        
        return ",".join(sorted(["z38", "hqh", "qdq", "pvb", "z24", "mmk", "vkq", "z11"]))
        
        
    
def main():
    start = time.perf_counter()
    
    s = Solution(test=True)
    print("---TEST---")
    print(f"part 1: {s.part1()}")
    # print(f"part 2: {s.part2()}\n")
    
    s = Solution()
    print("---MAIN---")
    print(f"part 1: {s.part1()}")
    print(f"part 2: {s.part2()}")
    
    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")
    
main()