package com.erikriosetiawan

fun main() {
    val str = "Erik Rio Setiawan"
    when {
        str.isEmpty() -> print("The String is empty!")
        str.length > 5 -> print("The String is short!")
        else -> print("The String is long!")
    }
}