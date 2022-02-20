#If you check out docs.python: int() function, you'll see that the int() function accepts an optional argument.
#As an example, write a program that asks the user for hexadecimal number as input.
#Then, use int() function to convert the input string to an integer (you'll need the second argument for this).
#Add 5 and display the result in hexadecimal format.


hex = int(input("Type a hexdecimal number on 0x format: "),16)
print(f"Your number +5 on hex is 0x{hex+5:x}")
