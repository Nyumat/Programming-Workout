# Programming Workout
# Originally Created 10/20/2020
def binarySearch(arr,left,right,target):
        
        arr = [1,2,3,4,5,20,50]
        target = 2
        
                mid = l + (r - 1) // 2;
                
                if arr[mid] == target:
                        return mid
                elif arr[mid] < x:
                        left = mid + 1
                else:
                        r = mid - 1
        return "Element not present."


# Find the Largest elemenet in an array.

def findLargest(arr):
        max = arr[0]
    
        for i in arr:
                if i > max:
                        max = i
        return max 

print(findLargest([1,2,3,4,5,6,7,10,2,1,3,4,200,5,1000]))

# Find the smallest element in an array.

def findSmallest(arr):
        min = arr[0]
        for i in arr:
                if i < min:
                        min = i
        return min
print(findSmallest([6,2,5,100]))


#Given a string, str, 
# Find the first reccuring character.

def findReccur(reccuring):
reccuring = "wwddabcadd"
seen = set()

for letter in reccuring:
    if letter in seen:
        print(letter)
        break
    else:
        seen.add(letter) 
        
print(findReccur("wwddabcadd"))
# Output : w

# Given array of random numbers with n reccuring numbers, find the most reccuring character.
def findOccurances(nums):
    seen = set()
    for num in nums:
        if (num not in seen):
            seen.add(num)
        else:
            return num

print(findOccurances([2,1,1,2,3,1]))

# Output : 1

# Given a string, remove all vowels from it and return it.

def findDeriv(ret):
    ret = True
    coefficent = input("Enter a coefficent")

    power = input("Enter a power.")

    variable = input("Enter A variable.")
    ret = False
    
    while ret == False:
        derivative = power * coefficent
        power = power - 1
        variable = variable
        break

    return " ".join(derivative,variable,power)

print(findDeriv())

# Given a non-empty string of characters, chars, return
# the first reccuring character.

def findReccuring(chars):
    seen = {}
    for i in chars:
        if chars in seen:
            seen[chars] = i
        else:
            return i
        
print(findReccuring("CCABCABANBB"))

# OUTPUT: C

# Now, with the same format, do the same thing but find the first
# NON reccuring charatcer.

def firstNonReccuring(chars):
    reccur = {}
    for i in chars:
        if i not in reccur:
            reccur[chars] = i
            continue
        else:
            reccur[i]


print(firstNonReccuring("ADACBADB"))


def removeElement(nums,val):

    for i in nums:
        if nums[i] == val:
            nums.remove(nums[i])
        else:
            continue
        return nums, len(nums)

    
print(removeElement([1,2,4,3,5],4))

# Given an array of ints, return the duplicate number.

import random
# My Random Password Generator. *Python Implementation*
def generatePassword(passLen):
    returnValue = ""
    letters_nums = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
    for _ in range(0,passLen):
        character = random.choice(letters_nums)
        returnValue += character
    
    return returnValue
def randomPasswordGeneration(amount):
    for _ in range(0,amount):
        print(generatePassword(15))

print(randomPasswordGeneration(100005))
# Reverse a singly linked list.

def reverseLinkedList(list):
    for i in list: 
        addTwo = list[i] + list[i + 1]
        slot = i
        while not slot:
            if list[slot] + 1 = i:
                list[slot] += 1
                return value = list[slot[i]]
        for i in list:
            curr = list[slot]
            prev = list[slot - 1]
            next = list[slot + 1]
            slot += 1
            #[1,2,3,4]
            #[4,3,2,1]
            while curr != list[-1]:
                prev = list[slot - 1]
                next = list[slot]
                curr = next
    return list
                                    
reverseLinkedList([1,2,3,4])
# Output = [4,3,2,1]

# A forco number is an integer that when 1 is added to the number, it becomes even.
# Given an array of random numbers, find out if it contains forco numbers, by returning the index OR number itself.
# Constrains: 0<range<100 || Can you do this problem in O(N) time and constant space? Hint : Recursion. <.<

def findForcoNumbers(range,nums):
    seen = {}
    for i in forco:
        i += findForcoNumbers(0,[0,102,300])
        if forc not in seen:
            return forc
        else:
            seen[forco]
    for j in range(len)(foroc):
        if alpha:
            return seen
