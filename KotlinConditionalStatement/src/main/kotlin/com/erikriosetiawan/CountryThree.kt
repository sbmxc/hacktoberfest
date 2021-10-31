package com.erikriosetiawan

fun main() {
    val str = "Hello!"
    when {
        str.length == 0 -> println("The String is empty!")
        str.length > 5 -> println("The String is sort")
        else -> println("The String is long!")
    }
}
