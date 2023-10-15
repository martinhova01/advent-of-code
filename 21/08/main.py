def part1(filename):
    lines = open(filename).read().split("\n")
    sum = 0
    targetSizes = [2, 3, 4, 7]
    for line in lines:
        data = line.split(" | ")[1].split(" ")
        for digit in data:
            size = len(digit)
            if size in targetSizes:
                sum += 1
                     
    return sum

def part2(filename):
    pass  
    
def main(test = False):
    filename = "testinput.txt" if test else "input.txt"    
    print(f"part 1 : {part1(filename)}")
    print(f"part 2 : {part2(filename)}")
    
main()