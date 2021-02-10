#Problem 540. Single Element in a Sorted Array


'''
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

Follow up: Your solution should run in O(log n) time and O(1) space.

 

Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: nums = [3,3,7,7,10,11,11]
Output: 10
 

Constraints:

1 <= nums.length <= 10^5
0 <= nums[i] <= 10^5

If every element in the sorted array were to appear exactly twice, they would occur in pairs at indices i, i+1 for all even i.

Equivalently, nums[i] = nums[i+1] and nums[i+1] != nums[i+2] for all even i.

When we insert the unique element into this list, the indices of all the pairs following it will be shifted by one, negating the above relationship.

So, for any even index i, we can compare nums[i] to nums[i+1].

If they are equal, the unique element must occur somewhere after index i+1
If they aren't equal, the unique element must occur somewhere before index i+1
Using this knowledge, we can use binary search to find the unique element.

We just have to make sure that our pivot index is always even, so we can use mid = 2 * ((lo + hi) // 4) instead of the usual mid = (lo + hi) // 2.
'''
def singleNonDuplicate(nums):
	#base case:
	if not nums:
		return None
	low, high = 0, len(nums)-1
	while low < high:
		mid = 2 * ((low+high) // 4)
		if nums[mid] == nums[mid+1]:
			low = mid + 2
		else: 
			high = mid
	return nums[low]		
#Time complexity: O(logn), binary search appraoch
#Space complexity: O(1)

#Main function to run the test case: 
def main():
	print("TESTING SINGLE ELEMENT IN SORTED ARRAY...")
	#test cases:
	nums =[1,1,2,3,3,4,4,8,8]
	print(singleNonDuplicate(nums))
	nums = [3,3,7,7,10,11,11]
	print(singleNonDuplicate(nums))	
	
	print("END OF TESTING...")
main()
