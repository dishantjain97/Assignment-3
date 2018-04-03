
print("Enter all the numbers in the list in a single line :")
num_list = [int(i) for i in input().strip().split()]
max_here=0
max =  num_list[0]
for num in num_list :
	max_here+=num
	if max_here >max :
		max = max_here
	if max_here<0:
		max_here = 0
print("maximum consecutive sum of integers",max)
