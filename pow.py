#Python3  program to solve the leet #50: Pow(x,n)
#Problem statement: 
'''
Implement pow(x, n), which calculates x raised to the power n (i.e. xn).
Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25

'''
def pow(x, n):
    #This approach contains memory error: 
    # #base case: 
    # if n == 0:
    #     return 1
    # if n == 1:
    #     return x
    # abs_n = abs(n)
    # x_array = [x] * abs_n
    # result = x_array[0]
    # # loop through the array and multiply each element together
    # for i in range(1, abs_n):
    #     result = result * x_array[i]
    # if n < 0: 
    #     return 1 / result
    # return result

    #base case: 
    if n == 0:
        return 1

    if n == 1: 
        return x

    temp = pow(x, int(n / 2))
    if(n % 2 == 0):
        return temp * temp 

    else: 
        if n > 0:
            return x * temp * temp 

        else: 
            return (temp * temp) / x

    




#driver code to run the program
def main():
    print("TESTING POWER IMPLEMENTATION...")
    test_val = 2.00000 
    n = -2
    print(pow(test_val, n))
    print("END OF TESTING...")
main()
