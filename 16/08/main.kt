import java.io.File
import java.security.MessageDigest
import java.util.Locale
import kotlin.collections.lastIndex
import kotlin.collections.dropLast
import kotlin.comparisons.compareByDescending


class Solution(var test: Boolean) {
    val filename: String = if (test) "testinput.txt" else "input.txt"
    val data: String = File(filename).readText().trim()
    val R = if (test) 3 else 6
    val C = if (test) 7 else 50
    var grid: MutableList<MutableList<Boolean>> = MutableList(R) {
        MutableList(C) {false}
    }

    fun print_grid(grid: MutableList<MutableList<Boolean>>) {
        var res = ""
        for (y in 0..grid.lastIndex) {
            for (x in 0..grid[y].lastIndex) {
                if (grid[y][x]) {
                    res += "#"
                }
                else {
                    res += " "
                }
            }
            res += "\n"
        }
        print(res)
    }

    fun part1(): Int {
        for (line in data.split("\n")) {
            val nums = Regex("\\d+").findAll(line).map { it.value.toInt() }.toList()

            if (line.startsWith("rect")) {
                for (x in 0..nums[0]-1) {
                    for (y in 0..nums[1]-1) {
                        grid[y][x] = true
                    }
                }
            }

            else if (line.startsWith("rotate row")) {
                var new_row: MutableList<Boolean> = MutableList(C){false}
                val y = nums[0]
                val shift = nums[1]
                for (x in 0..C-1) {
                    new_row[(x + shift) % C] = grid[y][x]
                }
                grid[y] = new_row
            }

            else if (line.startsWith("rotate column")) {
                var new_col: MutableList<Boolean> = MutableList(R){false}
                val x = nums[0]
                val shift = nums[1]
                for (y in 0..R-1) {
                    new_col[(y + shift) % R] = grid[y][x]
                }
                for (y in 0..R-1) {
                    grid[y][x] = new_col[y]
                }
            }
        }
        return grid.flatten().count{ it }
    }
    
    fun part2(): String {
        print_grid(grid)
        return "see above :)"
    }
}

fun main() {
    val start = System.nanoTime()

    var s = Solution(true)
    println("---TEST---")
    println("part1: " + s.part1() + "\n")
    
    s = Solution(false)
    println("---Main---")
    println("part1: " + s.part1())
    println("part2: " + s.part2() + "\n")

    val end = System.nanoTime()
    println("Time elapsed: ${String.format(Locale.US, "%.2f", (end - start) / 1_000_000_000.0)}s")
}