#Python3 program to implement Leetcode 74. Search a 2D Matrix

#Problem statememt: 
'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false

'''
#linear serach algorithm that would just go through the matrix 2D array linearly and search for the target
def searchMatrix_LINEAR_SEARCH(matrix, target):
    #base case: 
    if not matrix: 
        return False
    
    #search through the array linearly: 
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == target: 
                return True

    return False

#Binary search approach:
#Time complexity: o(logn x logn)
#we will perform two binary search, one for the outer layer to look for the element that matches the target
#The other one would be for comparing the last element of each row with the target value to pick which row that the target would be potentially be stored in
def searchMatrix_BINARY_SEARCH(matrix, target):
    #base case: 
    if not matrix or not matrix[0]: 
        return False

    #variable intialization: 
    left = 0
    right = len(matrix[0]) - 1
    #row that would contain the target value
    row = targetRow(matrix, target)

    #bianry search: 
    while left < right: 
        mid = (left + right) // 2 
        #THE TARGET IS GREATER THAN THE VALUE WE ARE LOOKING AT!!!!
        if(matrix[row][mid] < target):
            left = mid + 1

        else: 
            right = mid

    return matrix[row][left] == target


#Helper method to perform the second binary search to look for the row that would contain the target value
def targetRow(matrix, target):
    m = len(matrix)
    n = len(matrix[0])

    left = 0
    right = m - 1

    #binary search algorithm: 
    while left < right: 
        mid = (left + right) // 2 
        print(mid)
        # print(matrix[mid][n-1])
        #comapre the last element in each row with the target
        if(matrix[mid][n-1] < target):
            left = mid + 1

        
        else:
            right = mid
        

    return left
        
 
#driver code to run the program: 
def main():
    print("TESTING SEARCH A 2D MATRIX...")
    test_matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
    target = 3
    test_matrix_01 = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
    target01 = 13

    print(searchMatrix_LINEAR_SEARCH(test_matrix, target))
    print(searchMatrix_LINEAR_SEARCH(test_matrix_01, target01))
    print("")

    print(searchMatrix_BINARY_SEARCH(test_matrix, target))
    print(searchMatrix_BINARY_SEARCH(test_matrix_01, target01))

    print("END OF TESTING...")
main()