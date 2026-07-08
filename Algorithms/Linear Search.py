----------------------------------
#To find a value in an array

def linear_search(arr,target):
    for i in range(1,len(arr)):
        if arr[i]==target:
            print(target, "is in this list!\nIndex Position:",i)
    else:
        print("This value is not in this list!")

------------------------------------
