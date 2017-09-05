import math

#  Recursive function 
def answer(area):
	if(area<1 or area>100000):
		return
	elif(check_if_perfect_square(area)):
		answer_list.append(area)
	else:
		smaller_number = int(math.sqrt(area))
		smaller_perfect_square = smaller_number*smaller_number
		diff = area - smaller_perfect_square
		answer_list.append(smaller_perfect_square)
		answer(diff)

#  Newton's method to check if a number is a perfect square or not.
def check_if_perfect_square(num):
	i=1 
	sum=0
	while sum<num:
		sum += i
		if sum == num:
			return True
		i+=2
	return False
	
#  Working all of the possible range specified in the problem.
for i in range(1, 100001):
	answer_list = []
	answer(i)
	print answer_list
