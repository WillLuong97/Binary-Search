#Leetcode 153. Find Minimum in Rotated Sorted Array
#Problem statement: 
'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2] 
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0
'''

#The approach to finding element in a rotated sorted array is to find its inflection point
'''
Idea:
We have an array that have been sorted at some index unknown to us, let's call this index the inflection point (IP).
Side note: You can solve all the rotated array questions using inflection point technique... good for interviews, I've been asked this question in an onsite interview

We can identify the IP as: The only place where arr[IP] > arr[IP + 1] and arr[IP] > arr[IP - 1]. Basically the only element which is bigger than both left and right elements.
Let's take the following array as an example:
[4, 5, 0, 1, 2, 3].

Based on the characteristics above, we can conclude that 5 is the IP.
In addition, we can see that elements from index 0...IP [0, IP] and [IP + 1, n ] are always increasing, from this we can infer that is it enough for us to compare min(arr[0], arr[IP + 1]) for our answer.

Edge case: no inflection point, IP will be the last index. So if IP == n - 1 just return arr[0]
'''
def findMin(nums):
    #base case: 
    if not nums:
        return None


    #helper methodd to find the inflection point in the array
    def get_inflection_point(nums):
        #find the bound of the search space.
        left = 0
        right = len(nums) - 1

        #begin binary search
        while left <= right: 
            mid = (left + right) // 2

            #if the mid is the last element in the list or it is greater than the element on
            #the right side of it, then it is an inflection point
            if mid == len(nums) - 1 or nums[mid] > nums[mid + 1]:
                return mid

            if nums[mid] >= nums[left]:
                right = mid - 1

            else: 
                left = mid + 1

        return left

            


    #Edge case: if the inflection point is the last point in the array, then there is no rotation and the smallest element is the first element in the sorted array
    inflectionPoint = get_inflection_point(nums)

    if inflectionPoint == len(nums) - 1:
        return nums[0]

    return min(nums[0], nums[inflectionPoint + 1])


#main functiion to run the program
def main():
    print("FINDING MINIMUM IN SORTED ARRAY...")
    test_01 = [3,4,5,1,2]
    test_02 = [4,5,6,7,0,1,2]
    print(findMin(test_01))
    print(findMin(test_02))
    print("END OF TESTING...")
main()