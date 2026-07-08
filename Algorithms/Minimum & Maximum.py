--------------------------------
#To find the maximum value 

def maximum(arr):
    maximum=arr[0]
    for i in range(1,len(arr)):
        compare=arr[i]
        if compare > maximum:
            maximum=compare
    print("Maximum Mark:",maximum)

-------------------------------
#To find the minimum value

def minimum(arr):
    minimum=arr[0]
    for i in range(1,len(arr)):
        compare=arr[i]
        if compare < minimum:
            minimum=compare
    print("Minimum Mark:", minimum)

----------------------------------
