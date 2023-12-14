from itertools import product


def directions4() -> list:
    return [(0,1),(1,0),(0,-1),(-1,0)]

def directions8() -> list:
    return [(dx, dy) for dx, dy in product((-1,0,1), repeat=2) if not dx == dy == 0]

def adjacent4(x: int, y: int) -> list:
    return [(x + dx, y + dy) for dx, dy in directions4()]

def adjacent8(x: int, y: int) -> list:
    return [(x + dx, y + dy) for dx, dy in directions8()]