file_path = "usr/docs/file.txt"

#Write code to open and read the file into a variable

#Suboptimal
f = open(file_path, "r")
contents = f.read()
f.close()

#Best way
#Context manager
with open(file_path, "r") as f:
    contents = f.read()
    

"""In this challenge, establish if a given integer num is a Curzon number. If 1 plus 2 elevated to num is exactly divisible by 1 plus 2 multiplied by num, then num is a Curzon number.

Given a non-negative integer num, implement a function that returns True if num is a Curzon number, or False otherwise."""

def check_curzon(num):
    #if (1+(num**2))%(1+(num*2))==0:
    #   print("...")
    numerator= 1+(num**2)
    denomenator= 1+ (num*2)
    if numerator%denomenator==0:
        return True
    else:
        return False


num=int(input("Enter a number:"))
print(check_curzon(num))


"""In electronics, a digital-to-analog converter (DAC, D/A, or D-to-A) is a system that converts a binary representation of that signal into an analog output. An 8 bit converter can represent a maximum of 2^8 different values, with each successive value differing by 1/256 of the full scale value, this becomes the system resolution.

Create a function that takes a decimal number representation of a signal and returns the analog voltage level that would be created by a DAC if it were given the same number in binary.

While value range is 0-1023, reference range is 0-5.00 volts. Value and reference is directly proportional.

This DAC has 10 bits of resolution and the DAC reference is set at 5.00 volts.

Examples

V_DAC(0) ➞ 0

V_DAC(1023) ➞ 5

V_DAC(400) ➞ 1.96"""


def DAC_value(num):
    DAC_constant= (5/1023)
    return (num*DAC_constant)


number= int(input("Enter a number:"))
print(DAC_value(number))

"""
Create a function that takes a number as an argument and returns "Fizz", "Buzz" or "FizzBuzz".

    If the number is a multiple of 3 the output should be "Fizz".
    If the number given is a multiple of 5, the output should be "Buzz".
    If the number given is a multiple of both 3 and 5, the output should be "FizzBuzz".
    If the number is not a multiple of either 3 or 5, the number should be output on its own as shown in the examples below.
    The output should always be a string even if it is not a multiple of 3 or 5.

Examples

fizz_buzz(3) ➞ "Fizz"

fizz_buzz(5) ➞ "Buzz"

fizz_buzz(15) ➞ "FizzBuzz"
fizz_buzz(4) ➞ "4"
"""
def FizzBuzz(num):
    if num%15==0: #(num%3==0) and (num%5==0)
        return "FizzBuzz"
    elif num%3==0:
        return "Fizz"
    elif num%5==0:
        return "Buzz"
    else:
        return str(num)
        
def FizzBuzz(num):
    return "Fizz"*(num%3==0)+"Buzz"*(num%5==0) or str(num)

FizzBuzz = lambda num: "Fizz"*(num%3==0)+"Buzz"*(num%5==0) or str(num)

number = int(input("Enter the number:"))
print(FizzBuzz(number))

"""Write a function that takes a list of numbers and returns a list with two elements:

    1 - The first element should be the sum of all even numbers in the list.
    2 - The second element should be the sum of all odd numbers in the list.

Example

sum_odd_and_even([1, 2, 3, 4, 5, 6]) ➞ [12, 9]
# 2 + 4 + 6 = 12 and 1 + 3 + 5 = 9

sum_odd_and_even([-1, -2, -3, -4, -5, -6]) ➞ [-12, -9])

sum_odd_and_even([0, 0]) ➞ [0, 0])"""

#DRY - Don't Repeat Yourself - Don't write more code that is already used

lst = []

def sum_odd_and_even(lst):
    sum_even=0
    sum_odd=0
    new_list=[]
    for i in lst:
        if i%2==0:
            sum_even+=i
        else:
            sum_odd+=i
    new_list.append(sum_even)
    new_list.append(sum_odd)
    return new_list

#Filter => filter(function, list)


# num=int(input("Enter a number:"))
# lst.append(n)
while True:
    n=int(input("Enter the number:"))
    lst.append(n)
    ans=input("Would you like to add another number to your list?")
    if ans=="no":
        break
    
print(sum_odd_and_even(lst))