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









