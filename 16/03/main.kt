import java.io.File
import kotlin.collections.listOf

class Solution(var test: Boolean) {
    val filename: String = if (test) "testinput.txt" else "input.txt"
    val data: String = File(filename).readText().trim()
    val numbers: List<Int> = Regex("\\d+").findAll(data)
        .map {it.value.toInt()}
        .toList()

    fun part1(): Int {
        var sum = 0
        for (i in 0..numbers.size-3 step 3) {
            var triangle = numbers.slice(i..i+2).sorted()
            if (triangle[0] + triangle[1] > triangle[2]) {
                sum++
            }
        }
        return sum
    }

    fun part2(): Int {
        var sum = 0
        for (i in 0..numbers.size-9 step 9) {
            for (j in 0..2) {
                var triangle = listOf(numbers[i + j], numbers[i + j + 3], numbers[i + j + 6]).sorted()
                if (triangle[0] + triangle[1] > triangle[2]) {
                    sum++
                }
            }
        }
        return sum
    }
}

fun main() {
    var s = Solution(true)
    println("---TEST---")
    println("part2: " + s.part2() + "\n")
    
    s = Solution(false)
    println("---Main---")
    println("part1: " + s.part1())
    println("part2: " + s.part2())
}