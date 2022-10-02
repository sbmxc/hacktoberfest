package com.erikriosetiawan

fun main() {
    val x = "English"
    when (x) {
        "English" -> print("How are you?")
        "German" -> print("Wie geht es dir?")
        else -> print("I don't know that language yet :(")
    }

    val name = readLine()!!.trim()
    val names = listOf("John", "Sarah", "Tim", "Maggie")
    when (name) {
        in names -> print("I know that name!")
        !in names -> print("Argument was not in the range from 1 to 10")
        else -> print(name.length)
    }
}