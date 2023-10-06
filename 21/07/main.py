import math
class Crab:
    def __init__(self, pos):
        self.pos = pos
        
        
    def getDistanceTo(self, newPos):
        return abs(self.pos - newPos)
    
    def getFuelUsage_part2(self, newPos):
        distance = self.getDistanceTo(newPos)
        
        result = 0
        while distance > 0:
            result += distance
            distance -= 1
            
        return result 
    
    def getPos(self):
        return self.pos
    
    

def solve(inputfilename, part):
    crabs = []
    for crabPos in open(inputfilename).readline().split(","):
        crabs.append(Crab(int(crabPos)))
        
    highestPos = 0
    for crab in crabs:
        if crab.getPos() > highestPos:
            highestPos = crab.getPos()
    fuelUsages = {}
    bestFuelUsage = math.inf
    for i in range(highestPos):
        fuelUsage = 0
        for crab in crabs:
            distance = crab.getDistanceTo(i)
            
            if part == 1:
                fuelUsage += distance
            else:
                if distance not in fuelUsages:
                    fuelUsages[distance] = crab.getFuelUsage_part2(i)
            
                fuelUsage += fuelUsages[distance]
        if fuelUsage < bestFuelUsage:
            bestFuelUsage = fuelUsage
            
    return bestFuelUsage


def main(test = False):
    filename = "testinput.txt" if test else "input.txt"     
    print(f"part 1 : {solve(filename, 1)}")
    print(f"part 2 : {solve(filename, 2)}")
    
    
main()

