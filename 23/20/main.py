import math
import time
from collections import deque


class Component:
    def __init__(self, label):
        self.label = label
        self.state = False
        self.type = ""
        self.prevs = {}
        self.destinations = []
        

class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.components = self.parse()
        
        
    def parse(self):
        lines = open(self.filename).read().split("\n")
        components = {}
            #add the components
        for line in lines:
            source = line.split(" -> ")[0][1:]
            destinations = line.split(" -> ")[1].split(", ")
            
            if source not in components:
                components[source] = Component(source)
                
            for destination in destinations:
                if destination not in components:
                    comp = Component(destination)
                    components[destination] = comp
                comp = components[destination]
                components[source].destinations.append(comp)
                   
            #set the types 
        for line in lines:
            comp = line.split(" -> ")[0]
            if comp[0] == "%":
                components[comp[1:]].type = "%"
            elif comp[0] == "&":
                components[comp[1:]].type = "&"
                  
            #add the prevs  
        for comp in components.values():
            for dest in comp.destinations:
                dest.prevs[comp] = False
                
        return components
              
        
    def part1(self):
        buttonPushes = 1000
        highPulses = 0
        lowPulses = 0
        for _ in range(buttonPushes):
            q = deque()
            q.append((self.components["roadcaster"], False, None)) #(component, pulseType, prev_component)
            while q:
                comp, pulse, prev_comp = q.popleft()
                if pulse:
                    highPulses += 1
                else:
                    lowPulses += 1
                    
                if comp.type == "%":
                    if pulse:
                        continue
                    comp.state = not comp.state
                    for dest in comp.destinations:
                        q.append((dest, comp.state, comp))
                        
                elif comp.type == "&":
                    comp.prevs[prev_comp] = pulse
                    for dest in comp.destinations:
                        if all(x for x in comp.prevs.values()):
                            q.append((dest, False, comp))
                        else:
                            q.append((dest, True, comp))
                else:
                    for dest in comp.destinations:
                        q.append((dest, pulse, comp))
                        
        return lowPulses * highPulses
    
    def part2(self):
        self.components = self.parse() #reset states
        buttonPushes = 0
        cycles = {}
        while True:
            buttonPushes += 1
            q = deque()
            q.append((self.components["roadcaster"], False, None)) #(component, pulseType, prev_component)
            while q:
                comp, pulse, prev_comp = q.popleft()
    
                if prev_comp != None:
                    for c in ["bd", "bp", "pm", "xn"]:
                        if prev_comp.label == c and not pulse:
                            if c not in cycles:
                                cycles[c] = buttonPushes
                            if len(cycles) == 4:
                                return math.lcm(*cycles.values())
        
                if comp.type == "%":
                    if pulse:
                        continue
                    
                    comp.state = not comp.state
                    for dest in comp.destinations:
                        q.append((dest, comp.state, comp))
                        
                elif comp.type == "&":
                    comp.prevs[prev_comp] = pulse
                    for dest in comp.destinations:
                        if all(x for x in comp.prevs.values()):
                            q.append((dest, False, comp))
                        else:
                            q.append((dest, True, comp))
                else:
                    for dest in comp.destinations:
                        q.append((dest, pulse, comp))
                        
               
    
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