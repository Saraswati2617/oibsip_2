'''Idea: Random Password Generator
Description:
For Beginners: Create a command-line password generator in Python that generates random passwords based on
user-defined criteria, such as length and character types (letters, numbers, symbols). Allow users to specify 
password length and character set preferences.'''

#function to shuffle the password
def shuffle(ch):
    random.shuffle(ch)
    str=""
    for i in range(total_letters-1):
        str=str+ch[i]
    print(f"The password is : {str}")


import random
#intialization of password characters
lower_char=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r',
            's','t','u','v','w','x','y','z']
upper_char=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R',
            'S','T','U','V','W','X','Y','Z']
symbol_char=['@','#','$','&']
numbers=['0','1','2','3','4','5','6','7','8','9']

total_letters=int(input("Enter the total number of characters you want in your password: "))
num_lower=int(input("Enter the number of LOWER CASE alphabets you want in your password: "))
num_upper=int(input("Enter the number of UPPER CASE alphabets you want in your password: "))
num_digits=int(input("Enter the number of DIGITS you want in your password: "))
num_symbol=int(input("Enter the number of SYMBOLS you want in your password: "))
if total_letters>(num_lower+num_upper+num_digits+num_symbol):
    print("LESS NUMBER OF CHARACTER NUMBER INPUT.TRY AGAIN!!")
if total_letters<(num_lower+num_upper+num_digits+num_symbol):
    print("MORE NUMBER OF CHARACTER SET INPUT.TRY AGAIN!!")
if total_letters==(num_lower+num_upper+num_digits+num_symbol):
    ch=[]
    if total_letters==(num_lower+num_upper+num_digits+num_symbol):
        for i in range(num_lower):
            search=random.choice(lower_char)
            ch=ch+list(search)
        for j in range(num_upper):
            search=random.choice(upper_char)
            ch=ch+list(search)
        for k in range(num_symbol):
            search=random.choice(symbol_char)
            ch=ch+list(search)
        for l in range(num_digits):
            search=random.choice(numbers)
            ch=ch+list(search)
    else:
        if total_letters>(num_lower+num_upper+num_digits+num_symbol):
            print("LESS CHARACTER SET GIVEN")
        else:
            print("CHARACT SET OUT OF LIMIT")
    # print(ch)
    shuffle(ch)
    stop=False
    while(stop!=True):
        ask=input("Do you want to shuffle this password: Type 'yes' or 'no' :: ")
        if ask=="yes":
          shuffle(ch)
        else:
            print("Thank you!!")
            stop=True
