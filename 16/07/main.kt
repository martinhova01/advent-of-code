import java.io.File
import java.security.MessageDigest
import java.util.Locale
import kotlin.collections.lastIndex
import kotlin.collections.dropLast
import kotlin.comparisons.compareByDescending


class Solution(var test: Boolean) {
    val filename: String = if (test) "testinput.txt" else "input.txt"
    val data: String = File(filename).readText().trim()
    val ips = data.split("\n")

    fun is_abba(input: String, i: Int): Boolean {
        if (i > input.length - 4) {
            return false
        }
        return input[i] == input[i + 3] && input[i + 1] == input[i + 2] && input[i] != input[i + 1]
    }

    fun is_aba(input: String, i: Int): Boolean {
        if (i > input.length - 3) {
            return false
        }
        return input[i] == input[i + 2] && input[i] != input[i + 1]
    }

    fun support_TLS(ip: String): Boolean {
        var in_bracket = false
        var abba_outside = false
        for (i in 0..ip.lastIndex) {
            val c = ip[i]
            if (c == '[') {
                in_bracket = true
                continue
            }
            if (c == ']') {
                in_bracket = false
                continue
            }
            if (is_abba(ip, i) && in_bracket) {
                return false
            }
            if (!in_bracket && is_abba(ip, i)) {
                abba_outside = true
            }
        }
        return abba_outside
    }

    fun support_SSL(ip: String): Boolean {
        var aba_outside: MutableSet<String> = mutableSetOf()
        var aba_inside: MutableSet<String> = mutableSetOf()
        var in_bracket = false
        for (i in 0..ip.lastIndex) {
            val c = ip[i]
            if (c == '[') {
                in_bracket = true
                continue
            }
            if (c == ']') {
                in_bracket = false
                continue
            }
            if (is_aba(ip, i)) {
                if (in_bracket) aba_inside.add(ip.slice(i..i+2)) else aba_outside.add(ip.slice(i..i+2))
            }

        }
        for (aba in aba_outside) {
            for (bab in aba_inside) {
                if (aba[0] == bab[1] && aba[1] == bab[0]) {
                    return true
                }
            }
        }
        return false
    }

    fun part1(): Int {
        return ips.filter { support_TLS(it) }.size
    }

    fun part2(): Int {
        return ips.filter { support_SSL(it) }.size
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
    println("Time elapsed: ${String.format(Locale.US, "%.2f", (end - start) / 1_000_000_000.0)}s")
}