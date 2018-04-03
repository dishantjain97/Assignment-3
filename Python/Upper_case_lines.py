print("Enter a sequence of lines")
para = []
while True:
    line = input()
    if line == "":
        break
    para.append(line)
for line in para :
	print(line.upper())
