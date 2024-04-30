#Exercise 1:
#Write a program that tells the user whether a letter is a vowel or not

letter = "u"

#Turn the letter into a lowercase letter to make sure you don't have to check uppercase vowels
lower_letter = letter.lower()

#Compare the letter to all vowels, if it is the same as any vowel it is a vowel
if lower_letter == "a" or lower_letter == "e" or lower_letter == "i" \
or lower_letter == "o" or lower_letter == "u":
    print("This is a vowel")
#If not, it is not a vowel
else:
    print("This is not a vowel")

#OR: ____________________________________________________________________________

letter = "c"

#Turn the letter into a lowercase letter to make sure you don't have to check uppercase vowels
lower_letter = letter.lower()

#Create either a list:
vowels = ["a", "e", "i", "o", "u"]
#OR a tuple:
vowels = ("a", "e", "i", "o", "u")

#Check if the letter is inside the tuple of vowels using the (in) keyword
if lower_letter in vowels:
    print("This is a vowel")
else:
    print("This is not a vowel")


#-----------------------------------------------------------------------------------------
#Exercise 2:
#Write a program that prints whether an integer is in between 1000 and 2000. If it is not, 
#print whether it is lower than 1000 or higher than 2000

number = 1200

#Use if and elif to compare the number to 1000 and 2000
if number < 1000:
    print("This number is lower than 1000")
elif number > 2000:
    print("This number is higher than 2000")
else:
    print("This number is in between 1000 and 2000")

#OR: ____________________________________________________________________________
#You can basically do this in any arrangement
if 1000 <= number >= 2000:
    print("This number is in between 1000 and 2000")
elif number < 1000:
    print("This number is lower than 1000")
else:
    print("This number is higher than 2000")


#-----------------------------------------------------------------------------------------
#Exercise 3:
#Write a program that prints the sum of 3 given numbers, but if all 3 numbers are the 
#same it should print 4 times the sum of the 3 numbers.

first_number = 3
second_number = 7
third_number = 8

sum = first_number + second_number + third_number

#There is a lot of different possibilities here, 
#as long as you compare one number to both of the others it works
if first_number == second_number and second_number == third_number:
    print("These numbers are the same!\n"
          f"The sum of these numbers is {sum}\n"
          f"Multiplied by 4 this becomes {sum * 4}"
          )
else:
    print(f"The sum of these numbers is {sum}")

#OR: ____________________________________________________________________________
first_number = 11
second_number = 11
third_number = 11

sum = first_number + second_number + third_number

#Assign a bool to this variable that shows if the numbers are the same
same = first_number == second_number and second_number == third_number

if same:
    print("These numbers are the same!")

print(f"The sum of these numbers is {sum}")

if same:
    print(f"Multiplied by 4 this becomes {sum * 4}")

#-----------------------------------------------------------------------------------------
#Exercise 4:
#Write a program that finds the largest of 4 numbers.
first_number = 11
second_number = 11
third_number = 11
fourth_number = 13

largest = first_number

if largest < second_number:
    largest = second_number
if largest < third_number:
    largest = third_number
if largest < fourth_number:
    largest = fourth_number

print(f"The largest number is {largest}")

#OR: ____________________________________________________________________________
#Use max() function

largest = max(first_number, second_number, third_number, fourth_number)

print(f"The largest number is {largest}")

#-----------------------------------------------------------------------------------------
#Exercise 5:
#Write a program that calculates how much money someone has left after taxes, 
#given their income.
income = 99000

#Create a net income variable and assign it the income - the tax 
if income < 67000:
    net_income = income - (income * 0.24)
elif income < 97000:
    net_income = income - (income * 0.31)
else:
    net_income = income - (income * 0.34)

print(f"Your income after taxes is {net_income} euro's")

#-----------------------------------------------------------------------------------------
#Exercise 6:
#Write a program that takes a string with a maximum size of 5. 
#Do something different depending on the size of the string.

string = "Doger"

string_size = len(string)

#Letter * 6
if string_size == 1:
    print(string * 6)

#Switch letter positions
elif string_size == 2:
    #EITHER:
    print(string[::-1])
    #OR: ____________________________________________________________________________
    print(string[1] + string[0])

#Move last letter from back of the string to the front
elif string_size == 3:
    #string[2] = third character of string 
    #string[:2] = all characters until the third character (1 and 2)
    print(string[2] + string[:2])

#Print reverse of string
elif string_size == 4:
    print(string[::-1])

#Print string seperated by t
else:
    print(* string, sep="t")
    #OR: ____________________________________________________________________________
    print("t".join(string))

#-----------------------------------------------------------------------------------------
#Exercise 7:
#Write a program that gives the user a basic test with three questions. If they 
#have a question wrong stop the quiz, if they have it right give them the next question


#I used variables here, it's also fine if you used the input() function! (Even better if you did!)
answer_one = 10
answer_two = 12
answer_three = 14

print("What is 2*2?")
#If answer is correct, tell the user and continue
if answer_one == 4:
    print("That is correct!")

    #Note that this is in the first if-statement!
    #if the first answer is wrong we don't want to ask the second question
    print("Wat is 6/3?")
    if answer_two == 2:
        print("That is correct!")

        #Once again, the third question is in the second if-statement
        print("What is 9*9?")
        if answer_three == 81:
            print("Correct! You passed the test!")
        else:
            print("That is false, you failed the test")

    else:
        print("That is false, you failed the test")

else:
    print("That is false, you failed the test")