import java.io.File
import java.security.MessageDigest
import kotlin.collections.lastIndex
import kotlin.collections.dropLast


class Solution(var test: Boolean) {
    val filename: String = if (test) "testinput.txt" else "input.txt"
    val data: String = File(filename).readText().trim()
    val messageDigest = MessageDigest.getInstance("MD5")

    fun md5(input: String): String {
        val bytes = this.messageDigest.digest(input.toByteArray())
        return bytes.joinToString("") { "%02x".format(it) }
}

    fun part1(): String {
        var res = ""
        var i: Long = 0
        while (res.length < 8) {
            var hash = md5(data + i.toString())
            if (hash.startsWith("00000")) {
                res += hash[5]
            }
            i++
        }
        return res
    }

    fun part2(): String {
        var res: MutableList<Char> = mutableListOf('_', '_', '_', '_', '_', '_', '_', '_')
        var i: Int = -1
        var count = 0
        while (count < 8) {
            ++i
            var hash = md5(data + i.toString())
            if (hash.startsWith("00000")) {
                var idx = hash[5]
                if (!idx.isDigit()) {
                    continue
                }
                if (idx.digitToInt() > 7) {
                    continue
                }
                if (!res[idx.digitToInt()].equals('_')) {
                    continue
                }
                res[idx.digitToInt()] = hash[6]
                ++count

            }
        }
        return res.joinToString("")
    }
}

fun main() {
    val start = System.nanoTime()

    var s = Solution(false)
    println("---Main---")
    println("part1: " + s.part1())
    println("part2: " + s.part2() + "\n")

    val end = System.nanoTime()
    println("Time elapsed: ${(end - start) / 1_000_000_000}s")
}