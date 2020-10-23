#Problem 162. Find Peak Element

#Problem statement: 

'''
A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5 
Explanation: Your function can return either index number 1 where the peak element is 2, 
             or index number 5 where the peak element is 6.
Follow up: Your solution should be in logarithmic complexity.
'''
#Time complexity: O(n), we have to look for all element in the array once
#space complexity: O(1)
def findPeakElement_LINEAR_SEARCH(nums):
    #base case
    if not nums:
        return None

    #Loop through the array to find the peak element
    for i in range(len(nums)):
        if nums[i] > nums[i+1]:
            return i

    return  len(nums) - 1

#Binary search: Since we can return any kind of peak element, we can just split the array into partition with a sorted region
#if it is sorted, the we can perform binary search to find the peak element.
#Through binary search, we find the middle element in the array, and then we look at its neighbor, if its neighbor on the right is greater, which means the peak is on its right
#so we will look at its right partition of the array, if not, we look on its right
# def findPeakElement_BinarySearch_Recursive(nums):
#     #base case

#Time complexity: O(logn)
#Space complexity: O(1)
def findPeakElement_BinarySearch_Iterative(nums):
    #base case:
    if not nums:
        return None
    #create the bound of the 
    left = 0
    right = len(nums) - 1

    while left <= right: 
        mid = (left + right) // 2

        #if the current element is greater than one after it, 
        #then the peak would be on the lef tof it
        if nums[mid] > nums[mid + 1]:
            right = mid - 1

        else:
            left = mid + 1

    return left


#Main function to run the program
def main():
    print("TESTING FIND PEAK ELEMENT...")
    test_num_1 = [1,2,3,1]
    test_num_2 = [1,2,1,3,5,6,4]

    print(findPeakElement_LINEAR_SEARCH(test_num_1))
    print(findPeakElement_LINEAR_SEARCH(test_num_2))

    print(findPeakElement_BinarySearch_Iterative(test_num_1))
    print(findPeakElement_BinarySearch_Iterative(test_num_2))

    # print(findPeakElement_BinarySearch_Recursive(test_num_1))
    # print(findPeakElement_BinarySearch_Recursive(test_num_2))
    
    print("END OF TESTING...")
main()