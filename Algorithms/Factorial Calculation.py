----------------------------
#To calculate the factorial of a number

number = int(input("Enter a number:"))
list_no = []
factorial_product = 1
for i in range(1, number + 1):
    list_no.append(i)
    factorial_product = factorial_product * i
print("The first ", number, "numbers are:", list_no)
print("Factorial of ", number, "(", number, "!) = ", factorial_product)

-----------------------------
