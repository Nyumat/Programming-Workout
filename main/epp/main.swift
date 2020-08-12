
import Foundation

 //Random Programming problems I came up with myself (besides fizzbuzz). They're  all probably  Leetcode Very Easy besides the last one.

  main.swift

/* Write a program that given a number , returns a list multiplication table to that number.


 Test Case:
 5
 1 x 1 = 1
 2 x 2 = 4
 3 x 3 = 9
 4 x 4 = 16
 5 x 5 = 25

*/

var tablesSize = Int(readLine(strippingNewline: true)!)

for num in (1...tablesSize!) {

    let answer = num * num

    print("\(num)" + " * " + "\(num)" + " = " + "\(answer)")

}


// Write a program that prints the next 20 leap years.

var currentYear = Int(readLine(strippingNewline: true)!)

var nextYear = currentYear! + 20

var yearsToGo = (currentYear!...nextYear)

for year in yearsToGo{
    print(year)
}



// Write a program that reverses string

func reverseString(stringToReverse:String)  -> String   {
    var str = ""
    for char in  stringToReverse {
       str = "\(char)" + str
        }
    print(str)
    return str
}

_ = reverseString(stringToReverse: "Racecar")
 
 
 //ouput: "racecaR"



 Write the game of hangman.
 
 Level: Easy

var numTries = 5
print("Enter a word to try and guess")
let word = readLine()
var guessedIt : Bool = true
    
    let wordToGuess = [word]
    
    print("enter a letter")
    let letter = readLine()
    
   
    if (letter == word.contains(letter) {
        
        var guessedIt = false
        print(wordToGuess)
        
    }
    
}

while guessedIt == false {


}


/*
 Write a short program that prints each number from 1 to 100 on a new line.
 For each multiple of 3, print "Fizz" instead of the number.
 For each multiple of 5, print "Buzz" instead of the number.
 For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.
 */


func fizzBuzz() {
    
    for i in 1...100 {
                
            if( i % 3 == 0 && i % 5 == 0)
            {
            print("FizzBuzz")
           }
            else if (i % 3 == 0)
            {
            print("Fizz")
            }
            else if (i % 5 == 0)
            {
            print("Buzz")
            }
            else
            {
            print(i)
        }
    }
                    
}


fizzBuzz()
 


 // HackerEarth's first problem.

let num = Int(readLine(strippingNewline: true)!)
let str = readLine()
let newN = num! * 2
print("\(newN)" + "\n\(str!)")
 
 

// Traverse an array, arr of random numbers, and count each occurance of said number */


func travserseArray(value:Int,i:Int,range:Int){
    var counter = 0
    var arr = [Int]()
    var values = [Int]()
    
    for _ in 1...3 {
        print("Add numbers to look for.")
        let valuesInput = Int(readLine(strippingNewline: true)!)
        values.append(valuesInput!)
    }
    
    for _ in 1...i {
            let um = Int.random(in: 0...i)
            arr.append(um)
       }
    
    for num in arr {
        for v in values {
            if values[v] == arr[num] {
                counter = counter + 1
            } else {
                continue
            }
        }
    }
    switch counter {
    case let counter where  counter == 0:
            print("There are no occurances  of " + "\(values[value]) in  this array.")
            break
    case let counter  where counter >= 1:
            print("There are " + "\(counter)" +  " occurances of " + "\(values[value])")
    default:
        print("null")
    }
    print(arr)
}

travserseArray(value: 3,i:3,range:10)

