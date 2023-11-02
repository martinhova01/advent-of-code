import matplotlib.pylab as plt

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
    sensors = parse(filename)[0]
    print(sensors)
    
    for (x, y, d) in sensors:
        x_s = [x, x + d, x, x - d, x]
        y_s = [y - d, y, y + d, y, y - d]
        plt.fill(x_s, y_s)
    plt.plot(
        [0, maxValue, maxValue, 0, 0],
        [0, 0, maxValue, maxValue, 0],
    )
    # plt.xlim(left=3403959, right=3403961)
    # plt.ylim(top=3289728, bottom=3289730)
    plt.show()

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
        beaconX = int(points[3].split(",")[0])
        beaconY = int(points[4])
        sensors.append((x, y, dist(x, y, beaconX, beaconY)))
        beacons.add((beaconX, beaconY))
    return sensors, beacons


def main(test = False):
    filename = "testinput.txt" if test else "input.txt"    
    print(f"part 1 : {part1(filename, test)}")
    print(f"part 2 : {part2(filename, test)}")
    
main(True)