# Dylan Gagnon


# Line 6 - 23 is used to define the input numbers into their correct values, to later be called upon and printed
#Defines binary number input into bin() value
def binary(number):
    value = int(number)
    print(value, " in Binary : ", bin(value))

#Defines octal number input into oct() value
def octal(number):
    value = int(number)
    print(value, " in Octal : ", oct(value))

#Defines decimal number input into int() value, since int is automatically a decimal num
def decimal(number):
    value = int(number)
    print(value, " in Decimal : ", int(value))

#Defines hexadecimal number input into hex() value
def hexadecimal(number):
    value = int(number)
    print(value, " in Hexadecimal : ", hex(value))

# User Instructions
print (
    'When entering a number, please proceed as directed. \n For Decimal, place [0o] in front of the number \n For Binary, place [0b] in front of the number \n For Octal, place [0d] in front of the number \n For Hexadecimal, place [0x] in front of the number')
# Examples for user to follow, incase of confusion
print ('Examples: 0o555  ,  0b10001101  ,  0d77  ,  0xEF71')
# Line break from program instructions to user input
print('--------------------------------------------------------')

# User input, stored as value named 'number'
number = input('Please enter a number and the correct prefix   ')
result = 0

# The following reads the number based upon its prefix input
# If the prefix is 0b for binary, the program will print the input, followed by the proper mathamatic conversions, so on for 0d, 0x 0o
# The conversion part is not 100% original code of mine, it is the sum function, then I changed the math depending on the requirement, (ex 16** for hex)
# The len function is used to return the number of items in an object
# once it detects what type the input was, the program then continues to run the number input through each if statement, producing a value
if (number[:2] == '0b'):
    num_update = number[2:]
    print(num_update)
    result = sum([int(num_update[len(num_update)-i-1])*(2**i)
                 for i in range(len(num_update))])

elif (number[:2] == '0o'):
    num_update = number[2:]
    print(num_update)
    result = sum([int(num_update[len(num_update)-i-1])*(8**i)
                 for i in range(len(num_update))])

elif (number[:2] == '0x'):
    num_update = number[2:]
    print(num_update)
    result = sum(int(num_update[len(num_update)-i-1])*(16**i)
                 for i in range(len(num_update)))

# if its a decimal number all it needs to return is the int function
else:
    result = int(number)

print('_____________Result____________')
print('Binary Value     : ', bin(result))
print('Octal Value      : ', oct(result))
print('Decimal Value    : ', result)
print('HexDecimal Value : ', hex(result))

print(result)
