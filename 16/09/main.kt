import java.io.File
import java.util.Locale


class Solution(var test: Boolean) {
    val filename: String = if (test) "testinput.txt" else "input.txt"
    val data: String = File(filename).readText().trim()


    fun decompress(input: String): String {
        var res = ""
        var i = 0
        while (i < input.length) {
            if (input[i] != '(') {
                res += input[i]
            }
            else {
                var marker = Regex("\\d+").findAll(input, i).take(2).toList().map { it.value.toInt() }
                var j = 0
                while (true) {
                    if (input[i + j] == ')') {
                        break
                    }
                    j++
                }
                val len = marker[0]
                val repeat = marker[1]
                val slice = input.slice(i+j+1..i+j+len)
                for (k in 1..repeat) {
                    res += slice
                }
                i += j + len
            }
            i++
        }
        return res
    }

    fun part1(): Int {
        return decompress(data).length
    }

    fun decompress_length(input: String): Long {
        var sum: Long = 0
        var i = 0
        while (i < input.length) {
            if (input[i] != '(') {
                sum++
            }
            else {
                var end_bracket = input.indexOf(')', i)
                var marker = Regex("\\d+").findAll(input, i).take(2).toList().map { it.value.toInt() }
                val len = marker[0]
                val repeat = marker[1]
                val slice = input.slice(end_bracket+1..end_bracket+len)
                sum += decompress_length(slice) * repeat
                i = end_bracket + len
            }
            i++
        }
        return sum
    }
    
    fun part2(): Long {
        return decompress_length(data)
    }
}

fun main() {
    val start = System.nanoTime()

    var s = Solution(true)
    println("---TEST---")
    println("part1: " + s.part1())
    println("part2: " + s.part2() + "\n")
    
    s = Solution(false)
    println("---Main---")
    println("part1: " + s.part1())
    println("part2: " + s.part2() + "\n")

    val end = System.nanoTime()
    println("Time elapsed: ${String.format(Locale.US, "%.2f", (end - start) / 1_000_000_000.0)}s")
}