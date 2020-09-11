#Python3 implementation of leetcode 350 Intersection of Two Arrays II 

#Problem statement: 
'''
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
nums1 = [1,1,2,2]
nums2 = [2,2]



What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

'''
def intersect(nums1, nums2):
    #base case: 
    if not nums1 or not nums2: 
        return None

    result = []
    sorted_nums1 = sorted(nums1) 
    sorted_num2 = sorted(nums2)
    #pointer to point at each element in each array
    i = 0
    j = 0
    while i < len(nums1) and j < len(nums2): 
        if sorted_nums1[i] == sorted_num2[j]:
            result.append(sorted_nums1[i])
            i+= 1
            j += 1

        elif sorted_nums1[i] > sorted_num2[j]:
            j+= 1

        else:
            i+= 1

    return result

#driver code: 
def main():
    print("TESTING FIND INTERSECTION II...")
    nums1 = [4,9,5]
    nums2 = [9,4,8,4]
    print(intersect(nums1, nums2))
    print("END OF TESTING...")
main()