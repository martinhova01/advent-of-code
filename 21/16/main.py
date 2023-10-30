
def part1(filename):
    data = bin(int(open(filename).read(), 16))[2:]
    print(data)
    print(int(data, 2))


def part2(filename):
    pass



def main(test = False):
    filename = "testinput.txt" if test else "input.txt"    
    print(f"part 1 : {part1(filename)}")
    print(f"part 2 : {part2(filename)}")
    
main()