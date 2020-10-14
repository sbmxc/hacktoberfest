// This script is written in Brainfuck 
// It prints HELLO WORLD! on the console.
// You can use https://copy.sh/brainfuck/ to run this code.

++++++++++ //Cell 0 = 10(To run the loop 10 times) 
[ 
>+++++++ // Cell 1 = 7*10  for characters
>+++ // Cell 2 = 3*10  for space
<<- // Setting the pointer back to cell 0 & decrement 
]
>++.---.+++++++..+++. //HELLO
>++. //space
<++++++++.--------.+++.------.--------. //WORLD
>+. //Exclaimation (!)