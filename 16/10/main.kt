import java.io.File
import java.util.Locale


class Solution(var test: Boolean) {
    val filename: String = if (test) "testinput.txt" else "input.txt"
    val data: String = File(filename).readText().trim()
    var value_bot_mapping: MutableMap<Int, Int> = mutableMapOf()
    var bots: MutableMap<Int, Pair<Int, Int>> = mutableMapOf()

    var edges: MutableMap<String, MutableList<Triple<String, String, Int>> = mutableMapOf()

    init {
        for (line in data.split("\n")) {
            if (line.startsWith("value")) {
                var nums = Regex("\\d+").findAll(line).map { it.value.toInt() }.toList()
                val value = nums[0]
                val bot = nums[1]
                this.value_bot_mapping.put(value, bot)
            }
            else {
                var nums = Regex("\\d+").findAll(line).map { it.value.toInt() }.toList()
                var split = line.split("and")
                val bot = nums[0]
                val o1 = nums[1]
                val o2 = nums[2]
                if (split[0].contains("output") && split[1].contains("output")) {
                    this.bots.put(bot, 1000 + o1 to 1000 + o2)
                }
                else if (split[0].contains("output")) {
                    this.bots.put(bot, 1000 + o1 to o2)
                }
                else if (split[1].contains("output")) {
                    this.bots.put(bot, o1 to 1000 + o2)
                }
                else {
                    this.bots.put(bot, o1 to o2)
                }
            }
        }

        var visited = mutableSetOf<Int>()
        while (true) {
            var next = this.value_bot_mapping.values.filter { !visited.contains(it) }.
        }

        
    }

    fun part1(): Int {
        println(this.value_bot_mapping)
        println(this.bots)
        


        return 0
    }
    
    fun part2(): Int {
        return 0
    }
}

fun main() {
    val start = System.nanoTime()

    var s = Solution(true)
    println("---TEST---")
    println("part1: " + s.part1())
    println("part2: " + s.part2() + "\n")
    
    // s = Solution(false)
    // println("---Main---")
    // println("part1: " + s.part1())
    // println("part2: " + s.part2() + "\n")

    val end = System.nanoTime()
    println("Time elapsed: ${String.format(Locale.US, "%.2f", (end - start) / 1_000_000_000.0)}s")
}