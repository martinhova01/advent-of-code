from pathlib import Path


def part1(inputfilename):
    horizontalPosition = 0
    dept = 0
    with open(inputfilename) as f:
        for line in f.readlines():
            direction = line.split(" ")[0]
            value = int(line.split(" ")[1])
            
            if direction == "forward":
                horizontalPosition += value
            elif direction == "up":
                dept -= value
            else:
                dept += value
        
        return dept * horizontalPosition
            

def part2(inputfilename):
    horizontalPos = 0
    dept = 0
    aim = 0
    
    with open(inputfilename) as f:
        for line in f.readlines():
            direction = line.split(" ")[0]
            value = int(line.split(" ")[1])
            
            if direction == "forward":
                horizontalPos += value
                dept += aim * value
            elif direction == "up":
                aim -= value
            else:
                aim += value
        
        return dept * horizontalPos

def main(test = False):
    if test:
        filename = str(Path(__file__).parent / "testinput.txt")
    else:
        filename = str(Path(__file__).parent / "input.txt")
        
    print(f"part 1 : {part1(filename)}")
    print(f"part 2 : {part2(filename)}")
    
    
main()