# Binary Search

## Definition: 

- Binary search will search through a sorted array by repeatedly diving the serach interval in half. Begin with an interval 
covering the whole array. If the value of the search key is less than the item in the middle of the interval, then narrow down the interval to the lower half. Otherwise, I narrow it down to the upper half. Repeatedly check until the value is found or the interval is empty. 

- Binary search can only be performed on a sorted array

- The idea of the binary search is to use the information that the array is sorted and reduce the time complexity down to O(logn). 


## Algorithm

- We basically ignore half of the elements in just after one comparison

1. Compare x with the middle element
2. If x matches with the middle element, we return the mid index
3. Else if x is greater than the middle element, then x can only lie in the right half subarray after the right element. 
So we repeat this for the right half.
4. Else (x is smaller) repeat for the left half


## Implemnetation (Python)

- Recursive implementation of the Binary Search

```
#Python3 program for recursive binary search
#return index of the target in the array if present, else return -1
def binarySearch(arr, l, r, x):
	#base case: if the array contains element
	if r >= l:
		#extract the middle element in the array
		mid =  l + (r - l) // 2
		#if target is equal to middle value:
		if arr[mid] = x:
			return mid

		#if element is smaller than mid, then it 
		# can onnly be present in the left subarray
		elif arr[mid] > x:
			return binarySearch(arr, l, mid - 1, x)
		#otherwise, it should be in the right subarray
		else:
			return bianrySearch(arr, mid + 1, r, x)
	else: #the array does not contain any element to check
		return -1
``` 

-Iterative implementation of Binary Search (basically a two pointer on two ends of the array problem)

```
def binarySearch(arr, l, r, x):
	#base case: the array contain some element 
	while l <= r:
		mid = l + (r - l) // 2

		#check if x is present in mid
		if arr[md] == x:
			return mid

		#if x is greater, ignore the left half
		if arr[mid] < x:
			l = mid + 1

		#if x is smaller, then the element was not present
		else:	
			l = mid - 1

	#if we reach here, then the element was not found
	return -1
```
