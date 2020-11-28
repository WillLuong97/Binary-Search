#Problem 81. Search in Rotated Sorted Array II

#Problem statment: 

'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
Follow up:

This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
Would this affect the run-time complexity? How and why?

'''
#Binary Search to look for the target
def search(nums, target):
    #base case: 
    if not target and not nums:
        return True

    first = 0 
    last = len(nums) - 1
    #make sure that the left bound and right bound are always valid
    while first <= last: 
        mid = (first + last) // 2
        #base case: the target is found at the mid element
        if target == nums[mid]:
            return True

        if nums[first] > nums[mid]: #the right side of the array is sorted
            if target < nums[last] and target >= nums[mid]:
                first = mid + 1

            else: 
                last = mid - 1

        elif nums[first] < nums[mid]: #the left side of the array is sorted
            if target >= nums[first] and target < nums[mid]:
                last = mid - 1

            else: 
                first = mid + 1
        else:
            first += 1
                
    return False

#main function to run the program
def main():
    print('TESTING SEARCH IN SORTED ARRAY II...')
    nums01 = [2,5,6,0,0,1,2]
    target01 = 0

    nums02 = [2,5,6,0,0,1,2]
    target02 = 3
    nums03 = [1,1,3,1]
    target03 = 3

    print(search(nums01, target01))
    print(search(nums02, target02))
    print(search(nums03, target03))
    print("END OF TESTING...")

main()
