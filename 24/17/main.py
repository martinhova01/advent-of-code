import time
import re

class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = open(self.filename).read().rstrip()
        self.parse()
        
        
    def parse(self):
        registers, program = self.data.split("\n\n")
        self.A, self.B, self.C = [int(x) for x in re.findall(r"\d+", registers)]
        self.program = [int(x) for x in re.findall(r"\d+", program)]
        
        
    def part1(self):
        out = []
        pc = 0
        while pc < len(self.program):
            opcode = self.program[pc]
            operand = self.program[pc + 1]
            
            # combo operands
            if opcode in (0, 2, 5, 6, 7):
                assert operand < 7
                if operand == 4:
                    operand = self.A
                elif operand == 5:
                    operand = self.B
                elif operand == 6:
                    operand = self.C
                
            match opcode:
                case 0:
                    self.A = self.A // (2**operand)
                case 1:
                    self.B = self.B ^ operand
                case 2:
                    self.B = operand % 8
                case 3:
                    if self.A != 0:
                        pc = operand
                        continue
                case 4:
                    self.B = self.B ^ self.C
                case 5:
                    out.append(str(operand % 8))
                case 6:
                    self.B = self.A // (2**operand)
                case 7:
                    self.C = self.A // (2**operand)
            pc += 2
        
        return ",".join(out)
    
    def run(self, A):
        B, C = 0, 0
        pc = 0
        while pc < len(self.program):
            opcode = self.program[pc]
            operand = self.program[pc + 1]
            
            # combo operands
            if opcode in (0, 2, 5, 6, 7):
                assert operand < 7
                if operand == 4:
                    operand = A
                elif operand == 5:
                    operand = B
                elif operand == 6:
                    operand = C
                
            match opcode:
                case 0:
                    A = A // (2**operand)
                case 1:
                    B = B ^ operand
                case 2:
                    B = operand % 8
                case 3:
                    if A != 0:
                        pc = operand
                        continue
                case 4:
                    B = B ^ C
                case 5:
                    return operand % 8
                case 6:
                    B = A // (2**operand)
                case 7:
                    C = A // (2**operand)
            pc += 2
            
    def decode(self, i, string):
        if i == -1:
            return string
            
        target = format(self.program[i], "03b")
        for j in range(8):
            A = int(string + format(j, "03b"), 2)
            if format(self.run(A), "03b") == target:
                ret = self.decode(i - 1, string + format(j, "03b"))
                if ret == "":
                    continue
                return ret
        return ""
    
    def part2(self):
        result_string = self.decode(len(self.program) - 1, "")
        return int(result_string, 2)
    
    
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