#simple div

str_command = input("Please type command a + b or a-b: ")

num1 = ''
str_A = ''

num2 = ''
str_B = ''

operation = ''
'''
2.5 ^ 3
'''
for letter in str_command:
	print(letter)
	if letter == '+' or letter == '-' or letter == '*' or letter == '/' or letter == '^':
		if str_A == '':
			num1 = letter
		elif operation != '':
			num2 = letter
		else:
			operation = letter
	else:	
		if operation == '':
			str_A = str_A + letter
		else:
			str_B = str_B + letter

str_A = num1 + str_A.strip()
str_B = num2 + str_B.strip()
print(str_A)
print(str_B)

#str_input = input("A: ")

delimoe = float(str_A)
#print(type(delimoe))

#operation = input ("+ / * - ^ : ") 

#str_input2 = input("B: ")
delitel = float(str_B)
#print(type(delitel))
result = None

if operation == '/':
    if delitel == 0:
    	result = 'Inf'
    else:
    	result = delimoe / delitel
#print(type(result))
elif operation == '+':
	result= delimoe + delitel
elif operation == '-':
	result = delimoe - delitel
elif operation == '*':
	result = delimoe * delitel
elif operation == '^':
	result = delimoe ** delitel

else: 
	result = "unknown"
#print(type(result))

print("Result: " + str(result))