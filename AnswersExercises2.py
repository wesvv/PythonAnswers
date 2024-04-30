#Exercise 1:
#Write a program that prints a string that introduces yourself(name, age, hobbies, etc.) that is
#at least a few sentences long. Use variables for at least your name, age and hobbies and put
#them in a formatted string.
name = "Wes"
age = 21
hobbies = "volleyball, programming and reading"
job = "mentor for Clarusway"
experience_years = 6

#note that this is divided over different lines. If you put it in one line it's too long
introduction = (
    f"I am {name}, I am {age} years old!\n"
    f"My hobbies are {hobbies} and my job is {job}.\n"
    f"I have programmed for {experience_years} years."
)

print(introduction)


#--------------------------------------------------------------------------------------------------
#Exercise 2:
#Write a program that prints a string made of three different variables using three different
#methods. (fstring, concatenation, .format, etc.)
first_string = "I am unwritten, "
second_string = "can’t read my mind, "
third_string = "I’m undefined."

print(f"{first_string}{second_string}{third_string}")
print(first_string + second_string + third_string, sep='')
print("{}{}{}".format(first_string,second_string,third_string))

#--------------------------------------------------------------------------------------------------
#Exercise 3:
#Write a program that prints whether a string is longer or shorter than 10 characters

sentence = "I am a super long sentence"

#Use len() to get the amount of characters in the string (or any listlike)
if len(sentence) > 10:
    print("This sentence is longer than 10 characters")
else:
    print("This sentence is shorter than or equal to 10 characters")

#--------------------------------------------------------------------------------------------------
#Exercise 4:
#Write a program that prints the reverse of a string if it’s length is a multiple of 3, 
#otherwise just print the string itself.

sentence = "I have 1 dog"

#Once again, use len() to get the amount of characters in the string (or any listlike)
#Use a variable here. You will need to use the length of the string multiple times in the script
length = len(sentence)

print(f"This string is {length} characters long")

if length % 3 == 0:
    #Use indexing to reverse a string by setting the step to -1
    print(sentence[::-1])
else:
    print(sentence)

#--------------------------------------------------------------------------------------------------
#Exercise 5:
#Write a program that prints a string that is made of the first 3 and last 3 
#characters of a given string

string = "Hello world"

#Get the first 3 characters of the string and concatenate the last 3 characters of the string
new_string = string[:3] + string[-3:]

print(new_string)

#--------------------------------------------------------------------------------------------------
#Exercise 6:
#Write a program that prints whether a number or string is a palindrome

number = 192

#Turn the number into a string
string = str(number)

#The reverse of the string is string[::-1], check if the reverse is the same as the string
if string == string[::-1]:
    print("This is a palindrome")
else:
    print("This is not a palindrome")