import copy
import math
import time
from collections import deque


class SFN():
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.parent = None
        
    def reduce(self):
        while True:
            if self.search_for_explode():
                continue
            if self.search_for_split():
                continue
            break
        
    def search_for_explode(self) -> bool:
        q = deque()
        q.append((self, 0)) #(node, height)
        visited = set()
        while q:
            u, height = q.popleft()
            
            visited.add(u)
            if height == 4:
                u.explode()
                return True
            if type(u.left) == SFN:
                u.left.parent = u
                q.append((u.left, height + 1))
                
            if type(u.right) == SFN:
                u.right.parent = u
                q.append((u.right, height + 1))
        return False
    
    def inorder_walk(self, l: list) -> list:
        if type(self.left) == SFN:
            self.left.inorder_walk(l)
            
        l.append(self)
        
        if type(self.right) == SFN:
            self.right.inorder_walk(l)
            
        return l
    
    def search_for_split(self):
        q = deque(self.inorder_walk([]))
        while q:
            u = q.popleft()
            
            if type(u.left) == int and u.left >= 10:
                u.left = SFN(u.left // 2, int(math.ceil(u.left / 2)))
                return True
            if type(u.right) == int and u.right >= 10:
                u.right = SFN(u.right // 2, int(math.ceil(u.right / 2)))
                return True
    
        return False
    
    def explode(self):
        self.add_left()
        self.add_right()
        if self.parent.left == self:
            self.parent.left = 0
        else:
            self.parent.right = 0
        
    def add_left(self):
        current = self
        while current.parent != None:
            if current.parent.left != current:
                
                if type(current.parent.left) == int:
                    current.parent.left += self.left
                    return
                
                #start traversing down
                current = current.parent.left
                while type(current.right) == SFN:
                    current = current.right
                current.right += self.left
                return
            current = current.parent
            
    def add_right(self):
        current = self
        while current.parent != None:
            if current.parent.right != current:
                
                if type(current.parent.right) == int:
                    current.parent.right += self.right
                    return
                    
                    
                #start traversing down
                current = current.parent.right
                while type(current.left) == SFN:
                    current = current.left
                current.left += self.right
                return
            current = current.parent
    

    
    def add(self, other):
        res = SFN(copy.deepcopy(self), copy.deepcopy(other))
        res.reduce()
        return res
    
    def magnitude(self):
        return (
            3 * (self.left.magnitude() if type(self.left) == SFN else self.left)
            + 2 * (self.right.magnitude() if type(self.right) == SFN else self.right)
        )
        
     
    def __str__(self):
        return f"[{self.left.__str__()}, {self.right.__str__()}]"
    
    def __repr__(self):
        return f"[{self.left.__str__()}, {self.right.__str__()}]"

class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data: list[SFN] = [self.list_to_SFN(eval(line)) for line in open(self.filename).read().split("\n")]
    
    def list_to_SFN(self, l) -> SFN:
        left, right = l[0], l[1]
        if type(left) == list:
            left = self.list_to_SFN(left)
        if type(right) == list:
            right = self.list_to_SFN(right)
        return SFN(left, right)
            
        
    def part1(self):
        sum = self.data[0]
        for i in range(1, len(self.data)):
            sum = sum.add(self.data[i])
        return sum.magnitude()
        
    
    def part2(self):
        best = 0
        for i in range(len(self.data)):
            for j in range(len(self.data)):
                if i == j:
                    continue
                mag1 = self.data[i].add(self.data[j]).magnitude()
                mag2 = self.data[j].add(self.data[i]).magnitude()
                best = max(best, mag1, mag2)
        return best
                
    
    
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