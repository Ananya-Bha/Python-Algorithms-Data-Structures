#TWO-DIMENSIONAL ARRAYS WORKSHEET
#------Section 1: Creating & Accesing a 2D Array
scores= [
    [45,67,89],
    [54,90,72],
    [61,88,95]
]
#1.1 & 1.2
print(scores[1][1])

for list in scores:
    for element in list:
        if element==90:
            print("90")


print(scores[2][0])
print(scores[0][0])
scores[0][0]=50
print(scores[0][0])


matrix=[]
for i in range(3):
    row=[]
    for j in range(3):
        value=int(input(f"Enter element [{i}][{j}]:"))
        row.append(value)
    matrix.append(row)

print(matrix)

#------ Section 2: Totalling & Averaging
#2.1 & 2.2

numbers=[
    [5,8,3],
    [7,2,6],
    [9,1,4]
]
total=0
for row in numbers:
    for element in row:
        total=total+element
print(total)


for i in range(3):
    row_total=0
    for j in range(3):
        row_total=row_total+numbers[i][j]
    print(f"Total for row {i+1} is {row_total}")

#------- Section 3: Max & Min
max=numbers[0][0]
for i in range(3):
    for j in range(3):
        if numbers[i][j]>max:
            max=numbers[i][j]
            Row=i
            Column=j

print(f"Maximum Value:{max}\nPosition: Row {i}, Column {j-2}")
min=numbers[0][0]
for i in range(3):
    for j in range(3):
        if numbers[i][j]<min:
            min=numbers[i][j]

print(min)

#----------- Section 4: Counting Values
marks=[
    [65,78,90],
    [45,55,60],
    [88,92,70]
]
count_70=0
count_50=0
for i in range(3):
    for j in range(3):
        if marks[i][j]>70:
            count_70+=1
        elif marks[i][j]<50:
            count_50+=1

print(f"Above 70: {count_70}\nBelow 50: {count_50}")
for i in range(3):
    row_above_70=0
    for j in range(3):
        if marks[i][j]>70:
            row_above_70+=1
    print(f"Row {i+1} has {row_above_70} values greater than 70.")


for i in range(3):
    row_max=marks[i][0]
    row_min=marks[i][0]
    for j in range(3):
        if marks[i][j]>row_max:
            row_max=marks[i][j]
        if marks[i][j]<row_min:
            row_min=marks[i][j]
    print(f"Student {i+1} highest is {row_max}")
