#Useful Binary Search template that can solve most problem. 

def template(searchArray):
	#base case: 
	if not searchArray:
		return None

	#Condition requirement: these are varies depends on the problem and it is up to the user to find the pattern 
	def condition(searchArray):
		#add code here: 
		pass

	left = 0
	right = len(searchArray) - 1

	while left < right: 
		mid = left + (right - left) // 2

		if condition(searchSpace): 
			right = mid

		else: 
			left = mid + 1
	return left

searchSpace = []
	
template(searchSpace)
