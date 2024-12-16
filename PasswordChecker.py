
clear = print("\n" * 1000)

print(f"""

{clear}, Clear, Clean, Cls or Blank = clear

Welcome! - By: UH4X
Original Github Repository: https://github.com/UH4X/PasswordChecker

This will check if you have a strong enough code!
Based on this coded point system, your password
will be tested and get a fast check if it meets 
the criteria for the strongest possible
password! ;)

Don't worry! This is a local runned Python program,
and so you will not be writing your code out
onto the internet, but rather locally where
it will be forgotten, if not saved by
unwelcome intruder alert.

Anyways, I hope you'll enjoy this app!

""")

#Weak - 3 or less points
#Moderate - 4-7 points 
#Strong - 7 and up

points = 0

def length():
    if len(user) >= 10:
        global points
        points += 4
        print("Psw-length - CHECK!")
    else:
        print("Length - MISSING! You need at least 10 Characters!")

#----------------------------------------------------------------------------------

def upper():

    upper_count = sum(char.isupper() for char in user)

    if upper_count >= 3:
        global points
        points += 2
        print("Uppercase - CHECK!")
    else:
        print("Uppercase - MISSING! You need at least 3 uppercases!")

#----------------------------------------------------------------------------------

def lower():

    lower_count = sum(char.islower() for char in user)

    if lower_count >= 4:
        global points
        points += 2
        print("Lowercase - CHECK!")
    else:
        print("Lowercase - MISSING! You need at least 4 lowercases!")

#----------------------------------------------------------------------------------

def digits():
 
    digits_count = sum(char.isdigit() for char in user)

    if digits_count >= 4:
        global points
        points += 3
        print("Digits - CHECK!")
        
    else:
        print("Digits - MISSING! You need at least 4 digits!")

#----------------------------------------------------------------------------------

def specials():

    special_chars = "!@#$%^&*()-_=+[]{};:'\",.<>?/\\|`~"
    special_count = sum(char in special_chars for char in user)

    if special_count >= 3:
        global points
        points += 5
        print("Specials - CHECK!")
        
    else:
        print("Specials - MISSING! You need at least 3 special character!")

#----------------------------------------------------------------------------------





def the_password():
    global points
    points = 0
    
            
    print("\n" * 500)
    print("Written Password:", user)
    print(f"Password length: {len(user)}")
    print()
    length()
    print()

    upper()
    print()

    lower() 
    print()

    digits() 
    print()

    specials()
    print()
    print()

    print(f"Your total score: {points}/16")
    print()
    print("Info:")

    if points == 16:
        print("You made it, your password has reached THE MAX! Your password is VERY STRONG!")
        print("Well done! :D")
        print()
    elif points == 2:
        print("I bet this could be bruteforced 😭, please improve it.")
        print()
    elif points <= 4:
        print("Your password is like an old grandma. Improve it.")
        print()
    elif points >= 6:
        print("Your password is okay. But please improve it just a little more. 😊")
        print()
    elif points >= 8:
        print("It keeps getting better and better! This is a pretty good password! :D")
        print()
    elif points >= 11:
        print("You don't have to improve it anymore, but rather stay safer than not. ;)")
    else:
        print("Your password is VERY WEAK, YOU HAVE to improve it.")
        print("Write it down or something.")
        print()


    

#2
#4
#6
#8
#11
#16
   


#----------------------------------------------------------------------------------#
#------------------------------RUNNING CODE!---------------------------------------#
#----------------------------------------------------------------------------------#

while True:
    try:
        print("Check Password? (Y/n)")
        command = input("Command: ").lower()
        print()


        if command in ["y", "yes"]:
            user = input("Enter Password: ")
            the_password() 

        if command in ["none", "clear", "clean", "cls", "blank"]:
            print("\n" * 1000)
        
    

    except ValueError:
        print("ERROR")