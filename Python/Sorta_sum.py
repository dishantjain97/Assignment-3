def sorta_sum(a,b):
	if a+b in range(10,20):
		return 20
	else:
		return a+b
print("Enter 2 numbers")
x = int(input())
y = int(input())
print("Sum of numbers is ",sorta_sum(x,y))