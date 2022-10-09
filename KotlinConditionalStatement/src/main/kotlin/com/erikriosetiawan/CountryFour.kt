package com.erikriosetiawan

fun main() {
    val hours = 8
    val str = when {
        hours < 8 -> "Not Meet"
        hours in 8..10 -> "Meet"
        else -> "Back"
    }
    println(str)
}