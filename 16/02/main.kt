import java.io.File

class Solution(var test: Boolean) {
    val filename: String = if (test) "testinput.txt" else "input.txt"
    val data: String = File(filename).readText().trim()
    val offsets: Map<Char, Pair<Int, Int>> = mapOf(
        'U' to Pair(0, -1),
        'D' to Pair(0, 1),
        'L' to Pair(-1, 0),
        'R' to Pair(1, 0)
    )
    val keypad: List<List<Char>> = listOf(
        listOf(' ', ' ', '1', ' ', ' '),
        listOf(' ', '2', '3', '4', ' '),
        listOf('5', '6', '7', '8', '9'),
        listOf(' ', 'A', 'B', 'C', ' '),
        listOf(' ', ' ', 'D', ' ', ' ')
    )

    fun part1(): String {
        var x: Int = 1
        var y: Int = 1
        var res: String = ""
        for (line in this.data.split("\n")) {
            for (c in line.trim()) {
                var (dx, dy) = offsets[c]!!
                if (x + dx >= 0 && x + dx <= 2) {
                    x = x + dx
                }
                if (y + dy >= 0 && y + dy <= 2) {
                    y = y + dy
                }
            }
        res += ((y * 3) + (x + 1)).toString()
        }
        return res
    }

    fun part2(): String {
        var x: Int = 0
        var y: Int = 2
        var res: String = ""
        for (line in this.data.split("\n")) {
            for (c in line.trim()) {
                var (dx, dy) = offsets[c]!!
                if (x + dx >= keypad[0].size || x + dx < 0 || y + dy >= keypad.size || y + dy < 0) {
                    continue
                }
                if (keypad[y + dy][x + dx].equals(' ')) {
                    continue
                }
                x += dx
                y += dy
            }
        res += keypad[y][x]
        }
        return res
    }
}

fun main() {
    var s = Solution(true)
    println("---TEST---")
    println("part1: " + s.part1())
    println("part2: " + s.part2() + "\n")
    
    s = Solution(false)
    println("---Main---")
    println("part1: " + s.part1())
    println("part2: " + s.part2())
}