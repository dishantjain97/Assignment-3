class StringTest :
	def __init__(self):
		self.str = ""
	def get_String_Input(self):
		self.str = input()
	def print_String_Upper(self):
		print(self.str.upper())

print("Enter a String")
String_Obj = StringTest()
String_Obj.get_String_Input()
print("Entered String in upper case :", end=" ")
String_Obj.print_String_Upper()
