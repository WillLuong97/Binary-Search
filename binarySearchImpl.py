#Python program to implement the binary search algorithm
#Binary search: also known as logarithmic search, is an algorithm to search through a sorted array by repeatedly dividing the search intervals in half
#Begin with an interval covering the whole array. If the target value is lesser than the value in the middle, narrow the interval to the lower half
#Otherwise, narrow it down to the upper half. Repeatedly check until the value is found or the interval is empty.
#Note: The idea is to use the information that the array is sorted and reduce the time complexity to O(logn)
#Time complexity; O(logn)


#Example: Given a sorted array of n element, write a function to search a given element x in arr[]
#recursive method: 
def binarySearch_RECURSION(arr, target, left, right):
    if right >= left:
        #extracting the middle element: 
        mid = left + (right - left) // 2

        #if the target value is the middle value: 
        if arr[mid] == target:
            return mid
        #if the target value is greater than the middle, call the function recursively on the right interval of the array
        elif arr[mid] > target:
            return binarySearch_RECURSION(arr, target, left, mid - 1)

        #if not, call the recursion on the left interval:
        else:
            return binarySearch_RECURSION(arr, target, mid + 1, right)
    else:
        #element is not in the array
        return -1


#Iterative method: 
def binarySearch_ITERATIVE(arr, target, left, right):
    while left <= right:
        #Extract the middle value
        mid = left + (right - 1) // 2
        #If the middle value is the same as target value
        if target == arr[mid]:
            return mid
        #if the target value is greater, ignore the left half
        elif target > arr[mid]:
            left = mid + 1
        #if the target value is lesser, ignore the right half
        elif target < arr[mid]:
            right = mid - 1
    else: 
        return  -1


#main function:
def main():
    print("**Binary Search Implementation**")
    arr = [2, 3, 4, 10, 40] 
    x = 10
    print(f"Find ", x, " in ", arr)
    print("Result: ")
    #Recursion:
    result = binarySearch_RECURSION(arr, x, 0, len(arr) - 1)
    if result != -1:
        print(f"Element is in the array", result)
    else:
        print("Not Found!")

    print("")
    #Iterative method: 
    result_2 = binarySearch_ITERATIVE(arr, x, 0, len(arr) - 1)
    if result != -1:
        print(f"Element is in the array", result_2)
    else:
        print("Not Found!")

    print("****************")

main()