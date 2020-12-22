
# Given a string, str, 
# Find the first reccuring character.
# Using Set
def findReccur(reccuring):
    seen = set()

    for letter in reccuring:
        if letter in seen:
            reccur = letter
        else:
            seen.add(letter) 
    return reccur
    
findReccur([A,B,A,B])
# Output : A

# Given array of random numbers with n reccuring numbers, find the most occuring character.
def findOccurances(nums):
    seen = set()
    for num in nums:
        if (num not in seen):
            seen.add(num)
        else:
            return num

print(findOccurances([2,1,1,2,3,1]))
# Output : 1

# Given a string, remove all vowels from it in place and return it.

def findDeriv():
    coefficent = input("Enter a coefficent")

    power = input("Enter a power.")

    variable = input("Enter A variable.")

    while True:
        derivative = power * coefficent
        power = power - 1
        variable = variable
        break

    return derivative,variable,power


print(findDeriv())

# Given a non-empty string of characters, chars, return
# the first reccuring char.

# Using a HashMap
def findReccuring(chars):
    seen = {}
    for i in chars:
        if chars in seen:
            seen[chars] = i
        else:
            return i
        
print(findReccuring("CCABCABANBB"))

# OUTPUT: C

# Now, do the same thing but find the first
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

# Given an array of elements and a number, remove the number from the array.
def removeElement(nums,val):

    for i in nums:
        if nums[i] == val:
            nums.remove(nums[i])
        else:
            continue
        return nums, len(nums)

    
print(removeElement([1,2,4,3,5],4))

import random
# Random Password Generator Python Implementation
def generatePassword(passLen):
    returnValue = ""
    letters_nums = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
    
    for _ in range(0,passLen):
        character = random.choice(letters_nums)
        returnValue += character
    
    return returnValue
    
def randomPasswordGeneration(amount):
    for _ in range(0,amount):
        print(generatePassword(10))

randomPasswordGeneration(1000000)
 
def reverseLinkedList(linkedLis):
    for i in linkedLis:
        prev = None 
        curr = head
        next = curr.next
        while True:
            curr.next = prev
            prev = curr
            curr = next
            next = curr.next
            if curr == None:
                head = prev
                break
    return prev

def countingSteps(steps,n):
    end = len(steps) - 1
    step_count = 0
    next_step = 0

    while next_step != end:
        step_count += 1
        if next_step == end:
            step_count += 1
            break
        else:
            continue
    return step_count
    
countingSteps([0,0,0],2)

def findForocoNum(numsEval):
    forco = 0
    for num in numsEval:
        num += 1
        for digit in num:
            if num[digit] + 2 == forco:
                return forco
            else:
                continue
        if forco > len(numsEval):
            return "No Forco nums"
        else:
            breakpoint
    return forco

"This is the counting islands problem from leetcode"
def numIslands(self, grid: List[List[str]]) -> int:
    def surroundCheck(binaryMatrix,i,j):
    lr = len(binaryMatrix)-1 #rows
    lc = len(binaryMatrix[0])-1

    if binaryMatrix[i][j]=="0":
        return
    binaryMatrix[i][j]="0" 
    if (i+1) <= lr:
         surroundCheck(binaryMatrix,i+1,j)
    if (j+1) <= lc:
        surroundCheck(binaryMatrix,i,j+1)
    if (i-1) >= 0:
        surroundCheck(binaryMatrix,i-1,j) 
    if (j-1) >= 0:
        surroundCheck(binaryMatrix,i,j-1)  
    numIsland=0
    for i in range(len(grid)):
       for j in  range(len(grid[0])):
          if grid[i][j]=="1":
            surroundCheck(grid,i,j)
            numIsland+=1
    return numIsland
def invertBinaryTree(tree):
    """
    We're going to be representing a tree 
    horizontally and not vertically because 
    unfortunately, im not skilled enough to create 
    a tree class myself yet. lol :(    

        Ex. [0,0,1,0,0]
            [0,2,0,3,0]
            [0,0,4,0,5]

        With the 0's representing empty tree links.

    *PS. While this IS more work to do as now we have
    a matrix versus an object, it's much more fun, because now we get
    to implement DFS, BFS, Backtracking, and Reccursion! :)

    """
    
def findNextNum(nums):
        """
        Given arr nums, the next num is the current indice plus
        the value of the current indicie.
        Now, with this array containing n numbers, return the next 
        num of the smallest digit.
        """
        
import random
# Given an array, nums containing numbers 1...100
# Find the number of missing integers.

nums = []
for x in range(0,100):
    nums.append(x)
    

def findMissingNums(nums):
    missingNum = {}
    miss_count = 0
    for i in nums:
        plusOne = i+1
        if plusOne not in nums:
            missingNum[i] = i + 1
            continue
        else:
            miss_count += 1
    print(miss_count)
findMissingNums(nums)

def plusOne(digits):
    for x in range(len(digits)):
        if digits[x] < 9:
            digits[x]+=1
        else:
            digits[x]=0
    print(digits)


plusOne([1,2,3,9])

def validPalindrome(s):
    begin = 0
    end = len(s) - 1
   
    while end > begin:
        if s[begin] == s[end]:
            begin+=1
            end-=1
            continue
        else:
            return False
            
    if begin >= end:
        return True

s = "tacocat"
print(validPalindrome(s))
#  Output: True

def sohw(digits):
    n = len(digits)-1
    while n>=0:
        if digits[n]<9:
            digits[n] += 1
            return digits
        digits[n] = 0
        n -= 1
    return [1] + digits


digits = [4,9,9,9]
print(sohw(digits))


def isPalindrome(s):

    begin = 0
    end = len(s) - 1

    while end > begin:
        if s[begin] == s[end]:
            begin+=1
            end-=1
            continue
        else:
            return False

    if begin >= end:
        return True
   
s = "hoh"
print(isPalindrome(s))


def makeGrid(cols,rows):
    board = []

    for row in range(rows):
        board.append([])
        for column in range(cols):
            board[row].append('x')

    return board
def printt(board):
    for row in board:
        print(" ".join(row))
       
board_obj = makeGrid(10,10)

printt(board_obj)


