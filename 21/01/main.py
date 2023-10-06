def part1(inputfilename):
    current = 0
    next = 0
    counter = 0

    with open(inputfilename) as f:
        for dept in f.readlines():
            dept = int(dept)
            if current == 0:
                current = dept
                
            else:
                next = dept
                if next > current:
                    counter += 1
                current = next
                
    return counter

def part2(inputfilename):
    sums = []
    with open(inputfilename) as f:
        lines = f.readlines()
        for i in range(2, len(lines)):
            sum = int(lines[i - 2]) + int(lines[i - 1]) + int(lines[i])
            sums.append(sum)
            
    previous = sums[0]
    current = 0
    counter = 0
    for i in range(1, len(sums)):
        current = sums[i]
        if current > previous:
            counter += 1
        previous = current
        
    return counter

def main(test = False):
    filename = "testinput.txt" if test else "input.txt"   
    print(f"part 1 : {part1(filename)}")
    print(f"part 2 : {part2(filename)}")
    
main()