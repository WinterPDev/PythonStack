// Use the generateCoinChange function below to receive a dollar (decimal) amount with change. 
// Covert that value to the number of quarters, dimes, nickels, and pennies it would have.
// It should count the number or quarters first then work it's way down from there
// This can return a string or an object or whatever you'd like

// Example: generateCoinChange(.67) would return 2 quarters, 1 dime, 1 nickel, 2 pennies
// Example: generateCoinChange(0.77) would return 3 quarters, 2 pennies
// Example: generateCoinChange(2.85) would return 11 quarters, 1 dime
// Example: generateCoinChange(4.57) would return 18 quarters, 1 nickel, 2 pennies

function generateCoinChange(input) {
    var money = Math.floor(input*100);
    var quarter = 25
    var dime = 10
    var nickel = 5

    var coins = {
    'quarters' : 0,
    'dimes' : 0,
    'nickels' : 0,
    'pennies' : 0
    }

    console.log(money)
    coins['quarters'] = Math.floor(money/quarter)
    money = money % quarter
    console.log (money)
    coins['dimes'] = Math.floor (money/dime)
    money = money % dime
    console.log (money)
    coins['nickels'] = Math.floor (money/nickel)
    money = money % nickel
    console.log (money)
    coins['pennies'] = money;

return coins;
}

console.log(generateCoinChange(.67)) 
console.log(generateCoinChange(0.77))
console.log(generateCoinChange(2.85)) 
console.log(generateCoinChange(4.57)) 