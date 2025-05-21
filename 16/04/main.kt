import java.io.File
import kotlin.collections.lastIndex
import kotlin.collections.dropLast


class Solution(var test: Boolean) {
    val filename: String = if (test) "testinput.txt" else "input.txt"
    val data: String = File(filename).readText().trim()
    var real_rooms: MutableList<String> = mutableListOf()

    fun part1(): Int {
        var sum = 0
        for (line in data.split("\n").map{it.trim()}) {
            val id: Int = Regex("\\d+").findAll(line).map{it.value.toInt()}.first()
            val checksum: String = line.slice(line.lastIndex-5..line.lastIndex-1)

            var names = line.split("-").dropLast(1)
            var count: MutableMap<Char, Int> = mutableMapOf()
            for (name in names) {
                for (c in name) {
                    if (!count.keys.contains(c)) {
                        count.put(c, 0)
                    }
                    count[c] = count[c]!! + 1
                }
            }

            if (count.keys.toList().sortedWith(compareByDescending<Char>{count[it]}.thenBy{it}).slice(0..4).equals(checksum.toList())) {
                sum += id
                real_rooms.add(line)
            }

        }
        return sum
    }

    fun part2(): Int {
        val alphabet = "abcdefghijklmnopqrstuvwxyz"
        for (line in real_rooms) {
            var plaintext = ""
            val id: Int = Regex("\\d+").findAll(line).map{it.value.toInt()}.first()
            for (c in line) {
                plaintext += alphabet[(alphabet.indexOf(c) + id) % alphabet.length]
            }
            if (plaintext.contains("northpole")) {
                return id
            }

        }
        return 0
    }
}

fun main() {
    var s = Solution(true)
    println("---TEST---")
    println("part1: " + s.part1() + "\n")
    
    s = Solution(false)
    println("---Main---")
    println("part1: " + s.part1())
    println("part2: " + s.part2())
}