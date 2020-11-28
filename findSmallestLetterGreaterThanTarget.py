#Leetcode 744. Find Smallest Letter Greater Than Target

'''
#Problem statement: 
Given a list of sorted characters letters containing only lowercase letters, and given a target letter target, find the smallest element in the list that is larger than the given target.

Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.

Examples:
Input:
letters = ["c", "f", "j"]
target = "a"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "c"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "d"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "g"
Output: "j"

Input:
letters = ["c", "f", "j"]
target = "j"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "k"
Output: "c"
Note:
letters has a length in range [2, 10000].
letters consists of lowercase letters, and contains at least 2 unique letters.
target is a lowercase letter.
'''
def nextGreatestLetter(letters, target):
    #base case: 
    if not letters or not target:
        return None

    left = 0
    right = len(target)

    while left <= right:
        mid = left + (right - left) // 2
        if letters[mid] == target:
            break

        elif letters[mid] <= target:
            left = mid + 1

        else: 
            right = mid - 1
    while left < len(letters) and letters[left] <= target:
        left += 1
    return letters[left] if left < len(letters) else letters[0]
#Main function to run the program: 
def main():
    print("TESTING FIND SMALLEST LETTER GREATER THAN TARGET...")
    letters_01 = ["c", "f", "j"]
    target_01 = "a"
    letters_02 = ["c", "f", "j"]
    target_02 = "c"
    letters_03 = ["c", "f", "j"]
    target_03 = "d"
    letters_04 = ["c", "f", "j"]
    target_04 = "g"
    letters = ["c", "f", "j"]
    target = "j"
    letters_05 = ["c", "f", "j"]
    target_05 = "k"
    print(nextGreatestLetter(letters, target))
    print(nextGreatestLetter(letters_01, target_01))
    print(nextGreatestLetter(letters_02, target_02))
    print(nextGreatestLetter(letters_03, target_03))
    print(nextGreatestLetter(letters_04, target_04))
    print(nextGreatestLetter(letters_05, target_05))
    print("END OF TESTING...")

main()