# Problem 0: Example
#
# This is a practice problem to help you understand how to write code in a 
# provided Python function.
#
# We'll create a function that checks a condition and prints a specific greeting
# message based on that condition.
#
# Requirements:
# - The function is named `print_greeting`.
# - Inside the function, declare a variable `python_is_fun` and set it to `True`.
# - Use a conditional statement to check if `python_is_fun` is `True`.
# - If `python_is_fun` is `True`, print the message "Python is fun!"

def print_greeting():
    # Your code goes here. Remember to indent!
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")

# Call the function
# print_greeting()


# Problem 1: Vowel or consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and 
#   determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user in the above
#   messages.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels. You may need to look up
#   how to use this online.
# - Ensure your code provides feedback for non-alphabetical or invalid entries.

def check_letter():
    # Your control flow logic goes here
    letter = input("Please enter a letter (a-z or A-Z)")
    letter = letter.lower()
    if letter in "aeiou":
        print(f"The letter {letter} is a vowel.")
    else:
        print(f"The letter {letter} is a consonant.")


# Call the function
# check_letter()

# Problem 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a
# user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative 
#   numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting
#   age.
# - Print a message indicating whether the user is eligible to vote based on the
#   entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure that you handle any 
#   conversion errors gracefully. You may need to look up how to do this online.
# - Use a conditional statement to check if the age meets the minimum voting age
#   requirement.

def check_voting_eligibility():
    # Your control flow logic goes here
    print("Welcome to the Check Voting Eligibility App! ")
    age =input("Please enter your age: ")
    
    try:
        age = int(age)
    except Exception as error:
        print("The value entered is not a valid number, please try again")
        check_voting_eligibility()

    voting_age = 18

    if age <= 0:
        print("Invalid Age, Please Try Again")
        check_voting_eligibility() # using recursion to call the fuction again and restart the process

    if age >= voting_age:
        print("The user is eligible to vote")
    else:
        print("The user is not eligible to vote")


# Call the function
# check_voting_eligibility()

# Problem 3: Calculate dog years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's
# age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the
#   dog's age.

def calculate_dog_years():
    # Your control flow logic goes here
    age = input("Input the dog's age: ")
    age = int(age)

    if age <= 0:
        print("Age must be a positive number")
    elif age <= 2:
        dog_years = age * 10
        print(f"The dog's age is dog years is {dog_years}")  
    else:
        dog_years = 20 + (age -2) * 7
        print(f"The dog's age is dog years is {dog_years}")    

# Call the function
# calculate_dog_years()

# Problem 4: Weather advice
#
# Write a Python script named `weather_advice` that provides clothing advice
# based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle
#   multiple conditions.

def weather_advice():
    # Your control flow logic goes here
    cold = input("Is it cold? (yes/no): ").lower()
    raining = input("Is it raining (yes/no): ").lower()

    if cold == "yes" and raining == "yes":
        print("Wear a waterproof coat.")
    elif cold == "yes" and raining == "no":
        print("Wear a warm coat")  
    elif  cold == "no" and raining == "yes":
        print("Carry and umbrella")
    else:
        print("Wear light clothing")   


# Call the function
# weather_advice()

# Problem 5: What's the season?
#
# Write a Python function named `determine_season` that figures out the season
# based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three
#   characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month:
#   "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in
#   <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure you validate the user's input and handle unexpected inputs
#   gracefully.

def determine_season():
    # Your control flow logic goes here
    month = input("Enter the month of the year (Jan - Dec)").strip().capitalize()
    day = int(input("Enter the day of the month:"))

    if month in ("Jan", "Feb") or (month == "Mar" and day <= 19) or(month =="Dec" and day >= 21):
        season = "Winter"
    elif month in ("April", "May") or (month == "Mar" and day >= 20) or (month == "Jun" and day <= 20):
        season = "Spring"
    elif month in ("Jul", "Aug") or (month == "Jun" and day >= 21) or (month =="Sept" and day <= 21):
        season = "Summer"
    else:
        season = "Fall"
    print(f"{month} {day} is in {season}") 
# Call the function
determine_season()




