#Python program to solve Leetcode 668 problem using Python and Binary Search approach:

'''
Problem statement: 
Nearly every one have used the Multiplication Table. But could you find out the k-th smallest number quickly from the multiplication table?

Given the height m and the length n of a m * n Multiplication Table, and a positive integer k, you need to return the k-th smallest number in this table.

Example 1:
Input: m = 3, n = 3, k = 5
Output: 
Explanation: 
The Multiplication Table:
1	2	3
2	4	6
3	6	9

The 5-th smallest number is 3 (1, 2, 2, 3, 3).
Example 2:
Input: m = 2, n = 3, k = 6
Output: 
Explanation: 
The Multiplication Table:
1	2	3
2	4	6

The 6-th smallest number is 6 (1, 2, 2, 3, 4, 6).
Note:
The m and n will be in the range [1, 30000].
The k will be in the range [1, m * n]

'''
def findKthNumber(m, n, k): 
	
	#helper method to define the condition of the binary search: 
	def enough(num):
		count = 0 
		for val in range(1, m+1):
			add = min(num // val, n)
			#early break
			if add == 0:
				return False
			count += add

		return count >= k 

	#define the upper and lowerbound of the search space
	left = 1
	right = n*m
	
	while left < right: 
		mid = left + (right - left) // 2

		#if the condition return true, then we will move the search space into the right partition
		if enough(mid):
			right = mid

		else: 
			left = mid + 1

	return left
	





def main():
	print("FINDING SMALLEST NUMBER IN THE MULTIPLACATION TABLE...")
	print(findKthNumber(3,3,5))
	print(findKthNumber(2,3,6))
	print("END OF PROGRAM...")


main()
