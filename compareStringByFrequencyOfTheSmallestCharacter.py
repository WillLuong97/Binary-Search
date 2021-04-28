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


Approach: I am going to solve this problem via a naive and linear approach: 
- Create a function f to calculate the frequency of the smallest lexicographical word in each words contains in both the queries and words array. 
-Afterward, iterate through each array and compare them together, if the f(queries[i]) < f(words[i]) => increment the counter by 1

Time complexity: O(n), the algorithm will have to look through all element in  both the arrays, calculate the frequency of each word conatin in both the array, then compare their frequency together. 
Space complexity: O(n), we have to store two array of lexico smallest word in both the queries and the words

'''
#Approach: we will find the smallest frequency of each words in each array, and once we have found them, we will comparing the two length together
def numSmallerByFrequency(queries, words):
	#create two arrays that store the frequencies of each smallest lexicograhical order of each string contains in both queries and words
	fqueries = [f(query) for query in queries]
	fwords = [f(word) for word in words]
	result = []
	#iterate through both the frequency array 
	for q in fqueries:
		#counter to count the number of word in words that are larger than queries in term of frequency
		counter = 0
		for w  in fwords:
			if q < w: 
				counter += 1
		result.append(counter)
	return result		

#helper method to return the frequency of the string with the smallest lexicographical order. 
def f(string):
	return string.count(min(string))
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
