def part1(filename, test):
    sensors, beacons = parse(filename)
    # print(beacons)
    
    row = 10 if test else 2000000
    overlaps = set()
    for sensor in sensors:
        ydist = abs(row - sensor[1])
        #no overlap
        if ydist > sensor[2]:
            continue
        x = sensor[0]
        r = sensor[2] - ydist
        overlaps.update(range(x - r, x + r + 1))
        
        
    #remove points where there is a beacon
    counter = 0
    for beacon in beacons:
        if beacon[1] == row:
            counter += 1
    return len(overlaps) - counter
    
    

def part2(filename, test):
    maxValue = 20 if test else 4000000
    pass

def dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def parse(filename):
    lines = open(filename).read().split("\n")
    sensors = []
    beacons = set()
    for line in lines:
        points = line.split("=")
        x = int(points[1].split(",")[0])
        y = int(points[2].split(":")[0])
        beaconCX = int(points[3].split(",")[0])
        beaconCY = int(points[4])
        sensors.append((x, y, dist(x, y, beaconCX, beaconCY)))
        beacons.add((beaconCX, beaconCY))
    return sensors, beacons


def main(test = False):
    filename = "testinput.txt" if test else "input.txt"    
    print(f"part 1 : {part1(filename, test)}")
    print(f"part 2 : {part2(filename, test)}")
    
main()