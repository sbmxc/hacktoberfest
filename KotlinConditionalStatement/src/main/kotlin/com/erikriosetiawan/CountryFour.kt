package com.erikriosetiawan

fun main() {
    val hours = 8
    val str = if (hours < 8) {
        "Not Meet"
    } else if (hours in 8..10) {
        "Meet"
    } else {
        "Back"
    }
    println(str)
}