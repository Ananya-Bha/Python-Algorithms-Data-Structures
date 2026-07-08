#Topic: One-dimensional arrays
--------------------------
#Q1)
def pass_s(student_scores):
    count = 0
    for i in student_scores:
        if i > 70:
            count = count + 1
    print("Students passed:", count)


def calculate_average(total, student_scores):
    Average = total / len(student_scores)
    print("Average:", Average)
    pass_s(student_scores)


def calculate_total(student_scores):
    total = 0
    for i in student_scores:
        total = total + i
    print("Total marks: ", total)
    calculate_average(total, student_scores)


student_scores = []
while True:
    print("Choos ans option:\n1.Enter student mark\n2.Quit")
    choice = input("> ")
    if choice == "1":
        marks = int(input("Enter student mark:"))
        student_scores.append(marks)
    elif choice == "2":
        calculate_total(student_scores)
        break
    else:
        print("Invalid input!")
---------------------------------------
#Q2)
max = student_scores[0]
index_value_m = 0
for i in range(1, len(student_scores)):
    compare = student_scores[i]
    if compare > max:
        max = compare
        index_value_m = i

print("Maximum value:", max, "\nAt index position ", index_value_m)

min = student_scores[0]
index_value = 0
for i in range(1, len(student_scores)):
    compare = student_scores[i]
    if compare < min:
        min = compare
        index_value = i
print("Minimum value:", min, "\nAt index position ", index_value)
------------------------------------------
#Q3)

def check_value(found,index_value):
    if found:
        print("Student ID found at index position ",index_value)
    else:
        print("Student ID not found")
        
Id_numbers=[1023,1045,1067,1098,1101,1120,1154]
check_id_value=int(input("Enter value needed to be searched:"))
index_value=0
found=False
for i in range(len(Id_numbers)):
    if check_id_value == Id_numbers[i]:
        found=True
        index_value=i
        break
check_value(found,index_value)
--------------------------------------------
#Q4)
def bubble_sort(numbers):
    n =len(numbers)
    for i in range(n):
        for j in range(0,n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j],numbers[j+1]=numbers[j+1],numbers[j]

           

numbers=[34,12,78,45,23,56]
bubble_sort(numbers)
print("sorted list:", numbers)
