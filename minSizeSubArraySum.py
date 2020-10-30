#209. Minimum Size Subarray Sum

#Problem statement: 
'''
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 
'''
#Function to solve the problem
#Sliding window approach:
def minSubArrayLen_WINDOW_SLIDING(s, nums):
    #base case: 
    if not nums: 
        return 0

    #create the boundary for the window
    left = 0 
    right = float('inf')
    #loop through the list of nums: 
    for index, value in enumerate(nums):
        s -= value
        while s <= 0:
            #Find appropriate bound of the window
            right = min(right, index - left + 1)
            s += nums[left]
            #increment the left window
            left += 1 
    return 0 if right == float('inf') else right
#Time complexity: O(n)
#Space complexity:  O(1)
#Binary Search method: 
def minSubArrayLen_BINARY_SEARCH(s, nums):
    pass


#Main function to run the solution
def main():
    print("TESTING MINIMUM SIZE SUBARRAY SUM...")
    test_s00 = 7
    test_nums00 = [2,3,1,2,4,3]

    print(minSubArrayLen_WINDOW_SLIDING(test_s00, test_nums00))
    print("END OF TESTING...")
main()