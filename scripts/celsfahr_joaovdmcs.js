//import
const readline = require('readline');
//criacao objeto
const rl = readline.createInterface({ input: process.stdin });


//function (celsius) {
//    let fahrenheit = (9/5) * celsius + 32;
//    console.log(`fahrenheit: ${fahrenheit.toFixed(1)}`);
//    rl.close();
//}

//process.stdout.write("Temperatura em Celsius: ");

rl.question('Celsius? ', celsius => {
    let fahrenheit = (9/5) * celsius + 32;
    console.log(`fahrenheit: ${fahrenheit.toFixed(1)}`);
    rl.close();
});
