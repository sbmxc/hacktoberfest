package com.erikriosetiawan

fun main() {
    val x = "German"
    val greeting = when (x) {
        "English" -> "How are you?"
        "German" -> "Wie geht es dir"
        else -> "I don't know that language yet :("
    }
    println(greeting)
}