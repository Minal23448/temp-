print ("hello")
H = int(input("ENTER THE HEIGHT: "))
W = int(input("ENTER THE WIDTH: "))
A = H*W

if H >= 0 and W >=0:
    print("Area of the rectangle is ",A)
else:
    print("INVALID INOUT")

------------------------------------

 2. Given a dictionary of students and their favourite colours:
# people={'Arham':'Blue','Lisa':'Yellow',''Vinod:'Purple','Jenny':'Pink'}
# a. Find out how many students are in the list
# b. Change Lisa’s favourite colour
# c. Remove 'Jenny' and her favourite colour

people={'Arham':'Blue','Lisa':'Yellow','Vinod':'Purple','Jenny':'Pink'}
name=len(people)
print("all member in list num :",name)
people["Lisa"]="pink"
print("lisa new colour",people)
del people['Jenny']
print("all list ",people)

------------------------------------
 #Even or Odd Check
num = 7
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
------------------------------------
Fibonacci Series
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

------------------------------------
Find Maximum in a List
nums = [4, 7, 1, 9]
max_val = max(nums)
------------------------------------

Check Palindrome
def is_palindrome(s):
    return s == s[::-1]


------------------------------------
 6. Reverse a String
s = "python"
reversed_s = s[::-1]
------------------------------------

# Check Prime Number
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

------------------------------------
# Factorial 
def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result
------------------------------------

. Sum of N Natural Numbers
n = 10
sum_n = n * (n + 1) // 2
------------------------------------

2. Swapping Two Variables
a, b = b, a

------------------------------------

1. Area of a Circle
import math
radius = 5
area = math.pi * radius ** 2
