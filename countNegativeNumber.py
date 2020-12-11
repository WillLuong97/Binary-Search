#Problem 1351. Count Negative Numbers in a Sorted Matrix


'''
Problem statement: 
Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise. 

Return the number of negative numbers in grid.
Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
Example 2:

Input: grid = [[3,2],[1,0]]
Output: 0
Example 3:

Input: grid = [[1,-1],[-1,-1]]
Output: 3
Example 4:

Input: grid = [[-1]]
Output: 1
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
-100 <= grid[i][j] <= 100

'''
def countNegatives(grid):
    #base case: 
    if not grid: 
        return None

    count = 0 
    #each of the grid array is sorted in the ascending order
    #function to find negative number using binary serach
    def binarySearch(array):
        #base case: 
        if not array: 
            return
        #getting the left and right boundary:
        left = 0
        right = len(array) - 1
        #running the binary search
        while left <= right:
            mid = left +(right - left) // 2
            if array[mid] >= 0:
                left = mid + 1

            else: 
                right = mid - 1

        return left
    #loop through the array to count the negatives:
    for i in range(len(grid)):
        count += (len(grid[0]) - binarySearch(grid[i]))
    return count
#main function to run the program: 
def main():
    print("TESTING COUNT NEGATIVE NUMBER IN A MATRIX...")
    grid_1 = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
    grid_2 = [[3,2],[1,0]]
    grid_3 = [[1,-1],[-1,-1]]
    grid_4 = [[-1]]
    print(countNegatives(grid_1))
    # print(countNegatives(grid_2))
    # print(countNegatives(grid_3))
    # print(countNegatives(grid_4))
    
    print("END OF TESTING...")
main()