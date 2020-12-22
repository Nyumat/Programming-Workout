import Foundation

// lessnewb.swift

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
 
// Traverse an unsorted array of "arr_size" random numbers of "num_range" range and for "search_amount" values.

func traverseArray(arr_size:Int,numRange:Int,searchAmount:Int){

var arr = [Int]()
var values = [Int]()
var count = 0
    
    for _ in 0..<searchAmount {
    print("Add values to look for.")
    let valuesInput = Int(readLine(strippingNewline: true)!)
    values.append(valuesInput!)
    }
    
    for _ in 0..<arr_size{
        let randomNumber = Int.random(in: 1...numRange)
        arr.append(randomNumber)
    }
    
    for num in arr {
        for v in (0..<values.count).reversed() {
                if num == values[v] {
                    count = count +  1
                } else {
                    continue        
                }
            }
    }
    print(arr)
    if count >= 0 {
    print("There are " + " \(count) instances of "  +  " \(values)")
    }
}
    
traverseArray( arr_size: 100, numRange: 100,searchAmount: 10)

/*
INPUT:
Add values to look for.
10
Add values to look for.
20
Add values to look for.
30
Add values to look for.
40
Add values to look for.
50
Add values to look for.
60
Add values to look for.
70
Add values to look for.
80
Add values to look for.
90
Add values to look for.
100

OUTPUT:
[31, 100, 74, 80, 50, 86, 65, 36, 37, 47, 76, 5, 2, 95, 85, 21, 52, 29, 68, 11, 1, 55, 69, 84, 4, 55, 83, 11, 80, 73, 98, 23, 46, 25, 47, 3, 83, 37, 6, 44, 27, 71, 75, 70, 57, 10, 40, 65, 91, 1, 45, 29, 31, 60, 13, 29, 69, 55, 34, 83, 75, 73, 80, 50, 70, 100, 14, 70, 89, 95, 58, 92, 53, 24, 79, 2, 28, 48, 87, 62, 37, 37, 55, 73, 98, 82, 15, 64, 48, 31, 81, 80, 18, 31, 63, 12, 91, 19, 75, 15]
There are  14 instances of [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
*/


// Traverse an array of "arr_size" size, containing random numbers, and count each occurance of N number. */

func traverseArray(number:Int,arr_size:Int,numRange:Int){

var arr = [Int]()
var count = 0
    
    for _ in 0..<arr_size{
        let randomNumber = Int.random(in: 1...numRange)
        arr.append(randomNumber)
    }
    
    for num in arr {
        if num == number {
            count = count +  1
        }
    
    }
    print(arr)
    print("There are " + " \(count) instances of "  +  " \(number)")
    
}
traverseArray(number: 1, arr_size: 50, numRange: 50)

/*

Output : [46, 48, 37, 10, 28, 1, 6, 33, 42, 15, 49, 46, 41, 20, 35, 49, 43, 2, 15, 17, 10, 29, 39, 35, 45, 8, 2, 33, 33, 16, 2, 11, 19, 33, 28, 15, 46, 12, 33, 47, 36, 35, 21, 41, 30, 7, 40, 16, 2, 38]
There are  1 instances of  1
O(n) time complexity
*/

/*
 You are given a string  word , which comprises English alphabets, determine the count of all the vowels in  word . Vowels are  [ a , e , i , o , u ] . Print the count of all the vowels that are available in the string  word .
 */

var a = "a"
var e = "e"
var i = "i"
var o = "o"
var u = "u"


func findVowels(word:String){
    
   var  arr = [String]()
    arr.append(word)
    
    var count: Int = 0
    
    for word in arr {
        for char in word {
            switch char {
                case "a":
                    count = count + 1
                case "e":
                    count = count + 1
                case "i":
                    count = count + 1
                case "o":
                    count = count + 1
                case "u":
                    count = count + 1
                default:
                    break
            }
        }
    }
    print("There are " +  "\(count) " + "vowels")
}
findVowels(word: "Hello! My name is Thomas.")

// Input: "Hello! My name is Thomas."
// Output : There are 7 vowels

*/

// Given an unsorted array of characters, arr, find the reoccuring character.

/*
Input - ["a","s","r","e","d","g","s"]
 
 Output - ["s"]
 
 */

func findReOccuringChars(charsToAd:Int) {
    
    var empty_arr = [String]()
    var evaluator_arr = [String]()
    var char_appreance = 0
    var appeared = [String]()
    
    
    for _ in 0..<charsToAd {
        let charsToAdd = readLine()!
        empty_arr.append(charsToAdd)
        evaluator_arr.append(charsToAdd)
            
        }

    
    
    for char in empty_arr {
        for i in (0..<evaluator_arr.count).reversed() {
            if char == evaluator_arr[i]{
                char_appreance = char_appreance + 1
                appeared.append(char)
                }
        
        }
        
    }

    for letter in evaluator_arr {
        for v in empty_arr{
            if letter == empty_arr[letter]  {
                print("Repeating char is " + "\(appeared[0])")
                }
        }
}
    if char_appreance == 0 {
        print("There are no repeating characters in this array")
    }
    
    }

print("--> Add Characters to evaluate")
findReOccuringChars(charsToAd: 5)


