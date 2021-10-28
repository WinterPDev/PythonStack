function isPal(arr) {
    for(var left=0; left<arr.length/2; left++) {
        // 0 < 5/2 = 2.5
        // left=1 1< 5/2 = 2.5
        var right = arr.length-1-left;
        // 5-1-0 = 4
        // 5-1-1 = 3
        if(arr[left] != arr[right]) {
        // [0] != [5] (1 == 1)
        // [1] != [2] ()
        // Not a palindrome!
            return "Not a pal-indrome!";
        }
    }
    return "Pal-indrome!";
}
    
var result1 = isPal( [1, 1, 2, 2, 1] );
console.log(result1);


// A Palindrome is a word, phrase, or sequence that reads the same backward as forward
// Examples: madam, civic, radar, level, rotor, kayak, refer, racecar, tacocat, etc.
// Use the isPalindrome function below to receive a string and return true if it's a Palindrome
// and false if it is not. Do not ignore whitespaces, casing matters!!

// Example 1: "racecar" returns true
// Example 2: "e tacocat e" returns true
// Example 3: "abba" returns true 
// Example 4: "Dud" returns false
// Example 5: "oho!" returns false
// Example 6: " to " returns false

// HINTS: You can loop through a string
// Figure out a way to compare one side of the string with it's opposite pair
// If those elements don't match then it's not a Palindrome
// If we make it through our loop and never hit false, then it should be a Palindrome

function isPalindrome(str) {
    for(i = 0; i < str.length/2; i++){
        var
    }
}

console.log(isPalindrome("racecar")); 
console.log(isPalindrome("e tacocat e"));
console.log(isPalindrome("abba")); 
console.log(isPalindrome("Dud")); 
console.log(isPalindrome("oho!")); 
console.log(isPalindrome(" to "));


function isPal(arr) {
    for(var left=0; left<arr.length/2; left++) {
        var right = arr.length-1-left;
        if(arr[left] != arr[right]) {
            return "Not a pal-indrome!";
        }
    }
    return "Pal-indrome!";
}

console.log(isPal("Dud"))

// Use the longestPalindrome function below to receive a string and return the 
// longest palindrome it can find in the whole string.  Include spaces as well!
// If the palindromes have the same length, keep the one most recently found

// Example 1: "my favorite racecar erupted" returns "e racecar e"
// Example 2: "nada" returns "ada"
// Example 3: "nothing to see" returns "ee"
// Example 4: "hello dada" returns "dad"
// Example 5: "not much" returns "n"

// HINTS: 
// --Think of how you could have a way to take one letter in the string and compare it with the rest 
//   of the string.  Then take the next letter and keep comparing.  Loops maybe? **nudge nudge**
// --Think of a way to combine longestPalindrome with isPalindrome.  You already have the functionality
//   of checking if something is a Palindrome so see if you can use it!

// The slice() method could be useful here, but if you find another way, great!

// FYI: slice() can select a range of characters in a string starting at a given index position and ending 
//      with, but not including, the other given index. 
// For example "hello".slice(1,4) would return "ell".  
// It starts at index position 1 which is "e" and ends, but doesn't includes, index position 4 which is "l"
function isPal(arr) {
    for(var left=0; left<arr.length/2; left++) {
        var right = arr.length-1-left;
        if(arr[left] != arr[right]) {
            return "Not a pal-indrome!";
        }
    }
    return "Pal-indrome!";
}

var test = "my favorite racecar erupted"

// Loop through the text 

function longestPalindrome(str) {
    var string_lsit = [];
    for(i = 0; i < str.length; i++){
        var left = str[i]
        var right = str.length-i;
        left == right
        var longestpal = ""
            if i == right
            longestpal = str.concat(i, right)
            console.log(longestpal)
        }
    }

longestPalindrome(test)


var test = "my favorite racecar erupted"

console.log(longestPalindrome("my favorite racecar erupted"));
console.log(longestPalindrome("nada"));
console.log(longestPalindrome("nothing to see"));
console.log(longestPalindrome("hello dada"));
console.log(longestPalindrome("not much"));