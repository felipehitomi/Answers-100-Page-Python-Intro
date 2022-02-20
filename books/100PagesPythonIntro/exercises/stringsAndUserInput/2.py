#Write a program to accept two input values.
#First can be either a number or a string value.
#Second is an integer value, which should be used to display the first value in centered alignment.
#You can use any character you prefer to surround the value, other than the default space character.

firstinput = input("Type a number or a string: ")
seccondinput = int(input("Type a number: "))
print(f"{firstinput:-^{seccondinput}}")
#precisava no seccondinput colocar {}
