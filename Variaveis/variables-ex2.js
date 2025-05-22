import {createInterface} from "readline";

const rl = createInterface({
    input: process.stdin,
    output: process.stdout,
});

var enteredNumbers = [];
var sumOfAllEnteredNumbers = 0;

function newNumber() {
    rl.question("Enter a number: ", (number) => {
        var transformStringToInt = parseInt(number);

        enteredNumbers.push(transformStringToInt);
        sumOfAllEnteredNumbers += transformStringToInt;

        rl.question("Do you want to continue? [0] - YES | [1] - NO: ", (answer) => {
            if (answer === "0") {
                console.log("------------------");
                newNumber();
            } else if (answer === "1") {
                console.log("------------------");
                console.log("Loading historic...");

                console.log("============= HISTORIC =============");
                console.log(`- All entered numbers: ${enteredNumbers};`);
                console.log(`- Quantity  of entered numbers: ${enteredNumbers.length}`);
                console.log(`- Sum of all entered numbers: ${sumOfAllEnteredNumbers}`);
                console.log("==========================");

                rl.close();
            }
        })
    })
}

newNumber();