#nested if


'''
Syntax:
if condition1:
    if condition2:
        statement1
    else:
        statement2  '''

'''
#eligibility of voting other / male (18-65) and female(21-45)
a=input("Enter your gender (male/female/other): ")
if a=="male" or a=="other":
    b=int(input("Enter your age: "))
    if 18<=b<=65:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")
elif a=="female":
    b=int(input("Enter your age: "))
    if 21<=b<=45:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")
else:
    print("Invalid gender entered.")  '''



# another code for same  question:- 
'''
gen=input('enter your gender : ')
if gen in ['male','female','other']:
    age=int(input('enter your age : '))
    if ((gen in['male','other'] and 18<=age<=65) or (gen=='female' and 21<=age<=45)):
        print('you are eligible to vote')
    else:
        print('you are not eligible to vote')
else:
    print('invalid gender entered correct gender')
'''

# wap to check the number is divisible by 3 and 7 or not 
'''
n=int (input('enter your number : '))
if n%3==0:
    if n%7==0:
        print(f'{n} is divisible by 3 and 7')
    else:
        print(f'{n} is divisible by 3 but not by 7')
else:
    print(f'{n} is not divisible by 3') '''




