import time

class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = open(self.filename).read().rstrip()
        
    def generate_filesystem(self):
        """Generate a filesystem based on the input. 
        The filesystem is a list of blocks `[pos, id, length]`, 
        where `pos` is the position of the block in the system, 
        `id` is the id of the block and 
        `length` is the length of the block

        """
        filesystem = []
        pos = 0
        for i in range(len(self.data)):
            length = int(self.data[i])
            if i % 2 == 0:
                filesystem.append([pos, i // 2, length])
            else:
                filesystem.append([pos, -1, length])
            pos += length
        return filesystem
        
    def part1(self):
        filesystem = self.generate_filesystem()
        free_block = 1
        data_block = len(filesystem) - 1
        
        while True:
            free_pos = filesystem[free_block][0]
            free_length = filesystem[free_block][2]
            
            data_id = filesystem[data_block][1]
            data_length = filesystem[data_block][2]
            
            if free_length < data_length:
                # fill this free block with data before going to the next free block
                filesystem[free_block][1] = data_id
                filesystem[data_block][2] = data_length - free_length
                free_block += 2
                
            elif free_length == data_length:
                # move the entire datablock to this free block
                filesystem[free_block][1] = data_id
                free_block += 2
                filesystem.pop(data_block)
                data_block -= 2
                
            else:
                # move the entire data block, but there is still free space left
                filesystem.insert(free_block, [free_pos, data_id, data_length])
                free_block += 1
                filesystem[free_block] = [free_pos + data_length, -1, free_length - data_length]
                
                filesystem.pop(data_block)
                data_block -= 1 # one has been inserted
                
            if free_block >= data_block:
                    break
                
        s = 0
        for block in filesystem:
            id = block[1]
            if id == -1:
                break
            pos = block[0]
            for offset in range(block[2]):
                s += (pos + offset) * id
        return s
    
    def find_first_free_block(self, filesystem) -> int:
        for i, block in enumerate(filesystem):
            if block[1] == -1:
                return i
        return -1
    
    def find_next_free_block(self, filesystem, current_free_block) -> int:
        for i in range(current_free_block + 1, len(filesystem)):
            if filesystem[i][1] == -1:
                return i
        return -1
            
    def find_data_block(self, filesystem, id):
        for i in range(len(filesystem) - 1, -1, -1):
            if filesystem[i][1] == id:
                return i
        return -1
              
    
    def part2(self):
        filesystem = self.generate_filesystem()
        
        biggest_id = filesystem[len(filesystem) - 1][1]
        
        for data_block_id in range(biggest_id, -1, -1):
            free_block = self.find_first_free_block(filesystem)
            data_block = self.find_data_block(filesystem, data_block_id)
            data_id = filesystem[data_block][1]
            data_length = filesystem[data_block][2]
            
            while True:
                free_pos = filesystem[free_block][0]
                free_length = filesystem[free_block][2]
                
                if free_length < data_length:
                    # not enough free space, find next free block
                    free_block = self.find_next_free_block(filesystem, free_block)
                    if free_block >= data_block or free_block == -1:
                        break
                    
                elif free_length == data_length:
                    # data fits, swap data and free space
                    filesystem[free_block][1] = data_id
                    filesystem[data_block][1] = -1
                    break
                    
                else:
                    # data fits, move data and update free block
                    filesystem[data_block][1] = -1
                    filesystem.insert(free_block, [free_pos, data_id, data_length])
                    filesystem[free_block + 1] = [free_pos + data_length, -1, free_length - data_length]
                    break      
                
        s = 0
        for block in filesystem:
            id = block[1]
            if id == -1:
                continue
            pos = block[0]
            for offset in range(block[2]):
                s += (pos + offset) * id
        return s
    
    
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