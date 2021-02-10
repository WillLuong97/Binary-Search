#Problem 1170. Compare Strings by Frequency of the Smallest Character

'''
Let the function f(s) be the frequency of the lexicographically smallest character in a non-empty string s. For example, if s = "dcce" then f(s) = 2 because the lexicographically smallest character is 'c', which has a frequency of 2.

You are given an array of strings words and another array of query strings queries. For each query queries[i], count the number of words in words such that f(queries[i]) < f(W) for each W in words.

Return an integer array answer, where each answer[i] is the answer to the ith query.

 

Example 1:

Input: queries = ["cbd"], words = ["zaaaz"]
Output: [1]
Explanation: On the first query we have f("cbd") = 1, f("zaaaz") = 3 so f("cbd") < f("zaaaz").
Example 2:

Input: queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]
Output: [1,2]
Explanation: On the first query only f("bbb") < f("aaaa"). On the second query both f("aaa") and f("aaaa") are both > f("cc").
 

Constraints:

1 <= queries.length <= 2000
1 <= words.length <= 2000
1 <= queries[i].length, words[i].length <= 10
queries[i][j], words[i][j] consist of lowercase English letters.

'''
import bisect
from collections import Counter
#Approach: we will find the smallest frequency of each words in each array, and once we have found them, we will comparing the two length together
def numSmallerByFrequency(queries, words):
	#base case:
	if not queries or not words:
		return None
	answer = []
	smallestWordFreqArr = []
	#loop through each array to count its word frequency
	for word in words:
		smallestFreqInWord = helper(word)
		smallestWordFreqArr.append(smallestFreqInWord)
	smallestWordFreqArr.sort()
	for query in queries: 
		smallestFreqInQuery = helper(query)
		insertionPoint = bisect.bisect_left(smallestWordFreqArr, smallestFreqInQuery)
		wordCount = len(smallestWordFreqArr) - insertionPoint
		answer.append(wordCount)
	return answer

#helper method to count the frequency of each words in each srting within each array
def helper(word):
	if not word:
		return
	#start counting the frequency in each letter:  
	counter = Counter(word)
	#getting the keys of each word
	keys = sorted(counter.keys())
	#we return the word with the smallest frequency
	return counter[keys[0]]	


	
#Main function to run the test cases:
def main():
	print("TESITNG COMPARE STRING BY FREQUENCY OF THE SMALLEST CHARACTERS...")
	queries_1 = ["cbd"]
	words_1 = ["zaaaz"]
	queries_2 = ["bbb","cc"]
	words_2 = ["a","aa","aaa","aaaa"]
	print(numSmallerByFrequency(queries_1, words_1))
	print(numSmallerByFrequency(queries_2, words_2))

	print("END OF TESTING...")
main()
