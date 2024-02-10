import time
import sympy


class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = self.parse()
        
    def parse(self):
        mapping = {}
        for line in open(self.filename).read().split("\n"):
            monkey, job = line.split(": ")
            mapping[monkey] = job
        return mapping
        
    def part1(self):
        return self.run("root")
    
    def part2(self):
        return self.solve_eq(self.get_eq("root"))
    
    def run(self, monkey):
        job = self.data[monkey]
        if "+" in job:
            sub = job.split(" + ")
            return self.run(sub[0]) + self.run(sub[1])
        elif "-" in job:
            sub = job.split(" - ")
            return self.run(sub[0]) - self.run(sub[1])
        elif "*" in job:
            sub = job.split(" * ")
            return self.run(sub[0]) * self.run(sub[1])
        elif "/" in job:
            sub = job.split(" / ")
            return self.run(sub[0]) // self.run(sub[1])
        else:
            return int(job)
        
    def get_eq(self, monkey):
        job = self.data[monkey]
        if monkey == "root":
            sub = job.split(" + ")
            return f"{self.get_eq(sub[0])} = {self.get_eq(sub[1])}"
        if "+" in job:
            sub = job.split(" + ")
            return f"({self.get_eq(sub[0])} + {self.get_eq(sub[1])})"
        elif "-" in job:
            sub = job.split(" - ")
            return f"({self.get_eq(sub[0])} - {self.get_eq(sub[1])})"
        elif "*" in job:
            sub = job.split(" * ")
            return f"({self.get_eq(sub[0])} * {self.get_eq(sub[1])})"
        elif "/" in job:
            sub = job.split(" / ")
            return f"({self.get_eq(sub[0])} / {self.get_eq(sub[1])})"
        elif monkey == "humn":
            return "x"
        else:
            return job
        
        
    def solve_eq(self, eq: str):
        lhs, rhs = eq.split(" = ")
        x = sympy.symbols("x")
        equation = sympy.Eq(eval(lhs), eval(rhs))
        return int(sympy.solve(equation, x)[0])
    
    
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