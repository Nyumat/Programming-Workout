# New Problem Set!
# All of these problems are indexed in line with leetcode.com 

#1. TwoSum

# Given an array arr and a target k, find two integers [x,y] that equal k.

def twoSum(arr, k):

    data = {}

    for i in range(len(arr)):
        match = k - arr[i]
        if match in data:
            return [data[match],i]
        else:
            data[arr[i]] = i
    
# Tests

twoSum = twoSum([1,2,3,3],6) # - > [2,3]
print(twoSum)

# 219. Contains Duplicate II

def containsDuplicateII(nums, k):
    map = {}

    for i in range(len(nums)):
        if nums[i] in map and i - map[nums[i]] <= k:
            return True
        map[nums[i]] = i
    return False


containsDuplicateII = containsDuplicateII([2,7,3,2,4],3) # - > True
print(containsDuplicateII)

# Binary Search Iteratively

def binarySearch(nums,target):
    if not nums:
        return []

    l = 0
    r = len(nums) - 1

    while (l < r):
        mid = l + (r - l) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
        # [1,2,3,4,5]
            l = mid + 1
        else:
            r = mid - 1
    return mid

binarySearch = binarySearch([1,2,3,4,5,6,7,8,9],2)
print(binarySearch)

# Valid Integer

def is_integer(string):
    counter = 0
    for i in string:
        if i >= '0' and i <= '9':
            counter += 1
    if counter == len(string):
        return True
    return False

valid_int = is_integer("99392")
print(valid_int)

# Valid Palindrome

def is_palindrome(str):
    left = 0
    right = len(str) - 1

    if str[left] == ' ':
        left +=1

    if str[right] == ' ':
        right -= 1    

    if not str:
        return True

    while (left < right):
        if str[left] != str[right]:
            return False
        else:
            left += 1
            right -= 1

    if left == right:
        return True

valid_palindrome = is_palindrome(" racecar ")
print(valid_palindrome)

# Valid Paraens

def valid_para(str):
    matches = {"[":"]",}
    stack = []

# A node contains the value, left and right pointers
class newNode: 
    def __init__(self,data): 
        self.data = data 
        self.left = self.right = None

# Invert Binary Tree
def invert(node):  
  
    if (node == None): 
        return
    else: 
  
        temp = node  
          
        # recursive calls
        invert(node.left)  
        invert(node.right)  
  
        # swap the pointers in this node
        temp = node.left  
        node.left = node.right  
        node.right = temp  

# print InOrder binary tree traversal.
def print_tree(node) : 
  
    if (node == None):  
        return
          
    print_tree(node.left)  
    print node.data,
    print_tree(node.right)  

root = newNode(2)  
root.left = newNode(1)  
root.right = newNode(4)  
root.right.left = newNode(3)  
root.right.right = newNode(5)  
  
# Print inorder traversal of the input tree
print("Inorder traversal of the constructed tree is")  
print_tree(root)  
      
# Convert tree to its mirror
invert(root)  
  
# Print inorder traversal of the mirror tree
print("\nInorder traversal of the mirror treeis ")  
print_tree(root)  
