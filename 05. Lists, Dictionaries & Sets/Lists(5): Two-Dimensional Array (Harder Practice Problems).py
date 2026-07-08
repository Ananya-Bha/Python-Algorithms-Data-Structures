#Python program Question 1---------------------------------------------

temperature=[[32,34,29,30,31,28,33],
             [27,29,31,30,32,28,29],
            [33,35,34,36,32,31,30],
            [29,28,30,31,32,33,34],
            [26,27,28,29,30,31,25]]

i = 1
for city in temperature:
    minimum = city[0]
    maximum = city[0]
    total = city[0]
    for v in range(1, len(city)):
        compare = city[v]
        total += compare
        if compare < minimum:
            minimum = compare
        elif compare > maximum:
            maximum = compare
    average=total/7
    print("City ",i,":","\n Maximum Temperature = ",maximum,"\n Minimum Temperature = ",minimum,"\n Average Temperature = ", average)
    i += 1

#Python program Question 2--------------------------------------------------

marks=[[85,78,92,88,76], 
      [79,85,80,70,90],
      [88,92,81,79,95],
      [70,75,65,80,72],
      [95,90,92,96,88]]

i = 1
for student in marks:
    minimum = student[0]
    maximum = student[0]
    total = student[0]
    for v in range(1, len(student)):
        compare = student[v]
        total += compare
        if compare < minimum:
            minimum = compare
        elif compare > maximum:
            maximum = compare
    average=total/7
    print("Student",i,":","\n Maximum Marks = ",maximum,"\n Minimum Marks = ",minimum,"\n Average Average Marks = ", average,"\nTotal Marks = ",total)
    i += 1

#Python question 3-------------------------------------------------

marks=[[85,78,92,88,76], 
      [79,85,80,70,90],
      [88,92,81,79,95],
      [70,75,65,80,72],
      [95,90,92,96,88]]
Total_marks=[]

i = 1
for student in marks:
    minimum = student[0]
    maximum = student[0]
    total = student[0]
    for v in range(1, len(student)):
        compare = student[v]
        total += compare
        if compare < minimum:
            minimum = compare
        elif compare > maximum:
            maximum = compare
    average=total/7
    Total_marks.append(total)
    print("Student",i,":","\n Maximum Marks = ",maximum,"\n Minimum Marks = ",minimum,"\n Average Average Marks = ", average,"\nTotal Marks = ",total)
    i += 1
min=Total_marks[0]
max=Total_marks[0]

for h in range(1,len(Total_marks)):
    compare = Total_marks[h]
    if compare < min:
        minimum = compare
    elif compare > max:
        maximum = compare
print("Highest total amrks in the c;ass is: ",max)
