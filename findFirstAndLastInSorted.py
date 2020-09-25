#Python program to find the first and last element in a sorted array

#Problem statemet: 
'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
nums is a non decreasing array.
-10^9 <= target <= 10^9
'''
#Binary search approach to maintain time complexity to O(logn)
def searchRange(nums, target):
    #result array: 
    result = []
    #perform a binary search on the left part of the list to find the left most element in the array
    leftMostIndex = partitionSearch(nums, target, True)

    if leftMostIndex == len(nums) or nums[leftMostIndex] != target: 
        return [-1, -1]

    #perform a binary seach on the right side of the list to find the right most element in the array
    rightMostIndex = partitionSearch(nums, target, False) - 1

    #append the left and right most index into the array
    

    return [leftMostIndex, rightMostIndex]

#helper method to perform binary search on the partition part of the array
def partitionSearch(nums, target, isLeft):
    low = 0
    high = len(nums)

    while low < high: 
        mid = (high + low) // 2
        #If we are dealing with the left part of the array, then if mid is the target, and we know that we are looking at 
        #left side, then recurse and keep looking at the left part of the array to see if there is any other element that is equal to 
        #the target but still on the left side.
        if nums[mid] > target or (isLeft and nums[mid] == target):
            high = mid
        #otherwise, keep looking through the right side until we finish the searching algorithm
        else: 
            low = mid + 1
    return low

#driver code to run the program 
def main():
    print("TESTING FIND FIRST AND LAST IN SORTED ARRAY...")
    nums = [5,7,7,8,8,10]
    target = 8
    target1 = 6
    print(searchRange(nums, target))
    print(searchRange(nums, target1))
    print("END OF TESTING...")
main()