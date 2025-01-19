## BUBBLE sort : 
def bubble_sort(arr): 
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1] , arr[j]
    return arr

array = [64, 34 , 25 , 12 , 22 , 11 , 90]
print("soted array: " , bubble_sort(array))

## Merge Sort : 
def merge_sort(arr):
    if len(arr) <=1:
        return arr
    mid = len(arr) // 2
    A_half = arr[:mid]
    B_half = arr[mid:]
    A_half = merge_sort(A_half)
    B_half = merge_sort(B_half)
    return merge(A_half , B_half)

def merge(left , right):
    n = []
    i,j = 0,0
    while i <len(left) and j <len(right):
        if left[i] < right[j]:
            n.append(left[i])
            i +=1
        else:
            n.append(right[j])
            j +=1

    n.extend(left[i:])
    n.extend(right[j:])
    return n

array = [10,30,50,40,60,80,101]
print("after merge list: " , merge_sort(array))

## Quick sort:
def quick_sort(arr , low ,high):
    if low < high:
        pivot = partition(arr , low , high)
        quick_sort(arr , low ,  pivot - 1)
        quick_sort(arr , pivot + 1 , high)
    return arr

def partition(arr , low , high):
    p = arr[low]
    i = low + 1
    j = high
    while True:
        while i <= j and arr[i] <= p:
            i +=1
        while i <= j and arr[j] >= p:
            j -=1
        if i < j:
            arr[i],arr[j] = arr[j],arr[i]
        else:
            break
    arr[low],arr[j] = arr[j],arr[low]
    return j

array = [int(x) for x in input("Enter a number :").split()]
sorted_array = quick_sort(array , 0 , len(array) - 1)
print("sorted elements are: " , sorted_array)

##### OR ########
array = [10, 90, 50, 60, 98, 80, 101]
sorted_array = quick_sort(array, 0, len(array) - 1)
print("After sorting:", sorted_array)


##insertiin sort
def insertion_sort(arr):
 
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
arr = [12, 11, 13, 5, 6]
print("Original array:", arr)
insertion_sort(arr)
print("Sorted array:", arr)

## SELECTON SORT
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
       min_index = i
       for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]

array = [64, 25, 12, 22, 11]
selection_sort(array)
print("Sorted array:", array)






