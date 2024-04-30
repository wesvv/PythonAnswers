#Exercise 1:
# Write a Python program to print the following string in the format shown below.

#Note that instead of putting it on one line, I divided it into three lines
#This is to make sure it doesn't make the lines too long/exceed the PEP character count
print(
    "Twinkle twinkle little star,\n\tHow I wonder what you are!\n"
    "\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\n"
    "Twinkle twinkle little star,\n\tHow I wonder what you are."
    )

#-----------------------------------------------------------------------------------------
#Exercise 2:
#Write a program that checks whether a number is even or odd and prints it.
number = 13

#Check the remainder of the number divided by 2
#If the number is even, the remainder is 0
if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

#OR:
#If the number is odd, the remainder is 1 
if number % 2 == 1:
    print("The number is odd")
else:
    print("The number is even")

#------------------------------------------------------------------------------------------
#Exercise 3:
#Write a program that has two integers, print their product(multiplication) only if the product is
#equal to or lower than 1000. Otherwise, print their sum(addition).
number_1 = 20
number_2 = 30

#Instead of using the same code multiple times, use variables
#They're better for readability and make the computer only have to do a calculation once
product = number_1 * number_2

#Put the result into a variable so you don't have to use the same print statement twice
if product <= 1000:
    result = product
else:
    result = number_1 + number_2

print(f"The result is {result}")

#------------------------------------------------------------------------------------------
#Exercise 4:
#Write a program that reverses a number between 100-999
number = 145
#Turn the number into a string
num_string = str(145)
#Reverse the string
reverse = num_string[::-1]

print(f"The reverse is {reverse}")

#OR:
#Use the modulus operator
number = 145
reverse = 0

#This line takes the remainder of the number divided by 10.
#This will give the first digit (in this case 5)
reverse += number % 10
#Then we do a floor division that removes the first digit from the number(in this case making number 14)
number //= 10

#We do the reverse * 10 to make space for the next number
reverse *= 10
#Then we do the same thing as before
reverse += number % 10
number //= 10

#We do this one more time
reverse *= 10
reverse += number % 10
number //= 10

print(f"The reverse is {reverse}")