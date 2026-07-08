-------------------------------------
#Sorting an array

def bubble_sort(array):
    size= len(array)
    for i in range(size):
        swaps = 0 #flag to detect if any swap occured
        for j in range (size- i-1):
            if array[j] > array[j+1]:# when tge current item is bigger than the next
                array[j], array[j+1]= array[j+1], array[j]
                swaps=1
        if not swaps:
            break # no swap in this pass, so array is sorted
    print("The sorted array is as follows:", array)

user_arr= list(input("Enter a list of number that you wnat to sort in ascending order: (Format--> [no1,no2,no3,etc]}\nEnter here:"))
bubble_sort(user_arr)

----------------------------------------
