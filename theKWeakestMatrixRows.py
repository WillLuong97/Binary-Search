#Leetcode 1337. The K Weakest Rows in a Matrix

'''
Given a m * n matrix mat of ones (representing soldiers) and zeros (representing civilians), return the indexes of the k weakest rows in the matrix ordered from the weakest to the strongest.

A row i is weaker than row j, if the number of soldiers in row i is less than the number of soldiers in row j, or they have the same number of soldiers but i is less than j. Soldiers are always stand in the frontier of a row, that is, always ones may appear first and then zeros.

Example 1:

Input: mat = 
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 
k = 3
Output: [2,0,3]
Explanation: 
The number of soldiers for each row is: 
row 0 -> 2 
row 1 -> 4 
row 2 -> 1 
row 3 -> 2 
row 4 -> 5 
Rows ordered from the weakest to the strongest are [2,0,3,1,4]
Example 2:

Input: mat = 
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]], 
k = 2
Output: [0,2]
Explanation: 
The number of soldiers for each row is: 
row 0 -> 1 
row 1 -> 4 
row 2 -> 1 
row 3 -> 1 
Rows ordered from the weakest to the strongest are [0,2,3,1]
 

Constraints:

m == mat.length
n == mat[i].length
2 <= n, m <= 100
1 <= k <= m
matrix[i][j] is either 0 or 1.

[1,0,0,0]
mid = 1
mid != 1
left = 0 
right = 0 
2nd iteration: 
mid = 0 
left = 0
right = 0
mid == 1

'''
#Binary search approach:
#The idea is to apply binary search to find the number of 1 in each rows and then compare them and return the one with the least amount, which would make it 
#the weakest row in the array
def kWeakestRows(mat, k):
    #base case: 
    if not mat: 
        return None

    #helper method to run the binary search algorithm
    #Array format: [1,...,0,0]
    def binarySearch(array):
        left = 0 
        right = len(array)  - 1
        count = 0 
        while left <= right: 
            mid = (left + right) //2 
            if array[mid] == 0: 
                right = mid - 1

            else: 
                count += (mid - (left - 1))
                left = mid + 1

        return count


    result = []
    for index, rows in enumerate(mat):
        result.append((binarySearch(rows), index))

    result.sort()

    return [result[i][1] for i in range(k)]

#main function to run the test cases
def main():
    print("TESTING THE KTH WEAKEST ROWS IN A MATRIX...")
    mat_1 = [[1,1,0,0,0],
            [1,1,1,1,0],
            [1,0,0,0,0],
            [1,1,0,0,0],
            [1,1,1,1,1]]
    k_1 = 3
    mat_2 = [[1,0,0,0],
            [1,1,1,1],
            [1,0,0,0],
            [1,0,0,0]]
    k_2 = 2
    print(kWeakestRows(mat_1, k_1))
    print(kWeakestRows(mat_2, k_2))


    print("END OF TESTING...")
main()