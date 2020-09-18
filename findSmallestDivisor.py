#Python3 implementation to solve leetcode 1283: Find the Smallest Divisor Given a Threshold using Binary search approach
#problem statement:
import math
'''
Given an array of integers nums and an integer threshold, we will choose a positive integer divisor 
and divide all the array by it and sum the result of the division. Find the smallest divisor such that the result mentioned above is less than or equal to threshold.

Each result of division is rounded to the nearest integer greater than or equal to that element. (For example: 7/3 = 3 and 10/2 = 5).

It is guaranteed that there will be an answer.

Example 1:

Input: nums = [1,2,5,9], threshold = 6
Output: 5
Explanation: We can get a sum to 17 (1+2+5+9) if the divisor is 1. 
If the divisor is 4 we can get a sum to 7 (1+1+2+3) and if the divisor is 5 the sum will be 5 (1+1+1+2). 
Example 2:

Input: nums = [2,3,5,7,11], threshold = 11
Output: 3
Example 3:

Input: nums = [19], threshold = 5
Output: 4

'''
def smallestDivisor(nums, threshold):
    #base case: 
    if not nums: 
        return None
    if not threshold: 
        return None
    
    def condition(divisor):
        #base case: 
        if not divisor:
            return None
        
        return sum((num - 1) // divisor + 1 for num in nums) <= threshold

    #setting the search space for the divisor
    left = 1
    right = max(nums)

    #as the divisor is outdie of the threshold level, the result would certainly be smaller but 
    #it would not the smallest divisor
    while left < right: 
        mid = left + (right - left) // 2

        if condition(mid):
            right = mid
        
        else: 
            left = mid + 1
    return left



#driver code: 
def main():
    print("TESTING FIND SMALLEST DIVISOR GIVEN A THRESHOLD...")
    test_nums_1 = [1,2,5,9]
    test_threshold_1 = 6
    test_nums_2 = [2,3,5,7,11]
    test_threshold_2 = 11
    test_nums_3 = [19]
    test_threshold_3 = 5

    print(smallestDivisor(test_nums_1, test_threshold_1))
    print(smallestDivisor(test_nums_2, test_threshold_2))
    print(smallestDivisor(test_nums_3, test_threshold_3))


    print("END OF TESTING...")
main()