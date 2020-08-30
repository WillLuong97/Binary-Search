#This python program uses Backtracking to solve the Binary Watch leetcode problem
#Problem statement: 
'''
Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.

Input: n = 1
Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]

'''

def readBinaryWatch(num):
    def dfs(LEDS, idx, hrs, mins, n):
        # base cases
        if hrs >= 12 or mins >= 60: #if the hours passed in is not in valid time format, the return nothing
            return
        if n == 0:     
            time = str(hrs) + ":" + "0"*(mins<10) + str(mins)
            result.append(time)
            return
        print(n, end=" ")
        if idx < len(LEDS):
            if idx <= 3:  # handle hours
                dfs(LEDS, idx+1, hrs + LEDS[idx], mins, n-1)
            else:  # handle minutes
                dfs(LEDS, idx+1, hrs, mins + LEDS[idx], n-1)
            dfs(LEDS, idx+1, hrs, mins, n)

    result = []
    LEDS = [
        8, 4, 2, 1,  # top row of watch
        32, 16, 8, 4, 2, 1 # bottom row of watch
    ]
    dfs(LEDS, 0, 0, 0, num)
    
    return result


#main function to run the program
def main():
    print("TESTING BINARY WATCH...")

    test_value = 1

    print(readBinaryWatch(1))

    print("End of testing...")

main()

