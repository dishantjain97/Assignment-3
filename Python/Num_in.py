def in1to10(num,outside_mode):
	if outside_mode :
		if num <=1 or num >=10 :
			return True
		else :
			return False
	else :
		if num in range(1,11) :
			return True
		else :
			return False
print("Enter a number")
num = int(input())
print("Enter outside mode")
user_answer = input().lower().strip()
if user_answer == "true":
        out_mode = True
elif user_answer == "false":
        out_mode = False
print("Num in 1 to 10 ",in1to10(num,out_mode))
