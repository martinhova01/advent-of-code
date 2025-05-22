import java.io.File
import java.security.MessageDigest
import kotlin.collections.lastIndex
import kotlin.collections.dropLast
import kotlin.comparisons.compareByDescending


class Solution(var test: Boolean) {
    val filename: String = if (test) "testinput.txt" else "input.txt"
    val data: String = File(filename).readText().trim()
    val word_length = data.split("\n")[0].length

    fun get_original_message(most_frequent: Boolean): String {
        var count: MutableMap<Pair<Int, Char>, Int> = mutableMapOf()
        for (line in data.split("\n") ) {
            for (i in 0..line.lastIndex) {
                val c = line[i]
                if (!count.keys.contains(Pair(i, c))) {
                    count.put(Pair(i, c), 0)
                }
                count[Pair(i, c)] = count[Pair(i, c)]!! + 1
            }
        }

        var res = ""
        for (i in 0..word_length-1) {
            val direction = if (most_frequent) -1 else 1
            var c = count.entries.filter { it.key.first == i }.toList().sortedBy{ direction * it.value }.first().key.second
            res += c
        }
        return res
    }

    fun part1(): String {
        return this.get_original_message(true)
    }

    fun part2(): String {
        return this.get_original_message(false)
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
    println("part2: " + s.part2())

    val end = System.nanoTime()
    println("Time elapsed: ${(end - start) / 1_000_000_000}s")
}