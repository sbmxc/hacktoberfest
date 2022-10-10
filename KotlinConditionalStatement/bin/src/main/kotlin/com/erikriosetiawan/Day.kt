package com.erikriosetiawan

enum class Day {
    Sunday,
    Monday,
    Tuesday,
    Wednesday,
    Thursday,
    Friday,
    Saturday
}

fun doOnDay(day: Day) {
    when (day) {
        Day.Sunday -> println("Holiday")
        Day.Monday -> println("Go to campuss")
        Day.Tuesday -> println("Create a new project")
        Day.Wednesday -> println("Coding in Android Studio")
        Day.Thursday -> println("Coding in Intellij IDEA")
        Day.Friday -> println("Learn Java")
        Day.Saturday -> println("Learn Kotlin")
        else -> println("Day not found!")
    }
}