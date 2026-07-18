# elif 
#syntax

'''
if condition1:
    statement1
elif condition2:
    statement2
else:
    statement3
'''


# 
'''
n= int(input(" enter your number: "))
if n==1:
             print("she is bhanu's gf")
elif n==2:
        print("she's ankita's gf")
else:
    print("she is not anyone's gf")
'''

#write a program to check enter integer is +ve , -ve or zero.
'''
a= int(input("enter your number:"))
if a>0:
        print(f"{a} is +ve number")
elif a<0:
    print(f"{a} is -ve number")
else:
       print(f"{a} is zero ")
'''

# write a program is even , odd or zero 
'''
n= int(input("enter your nummber:"))
if n%2==0:
    print(f"{n} is even number")
elif n%2 !=0:
    print(f"{n} is odd number")
else:
    print(f"{n} is zero")
'''
#write a program to check the char is upper case, lower case  or  numric string 
# and spacial character
a = input("enter your char: ")
if a.isupper():
    print(f"{a} is upper case")
elif a.islower():
    print(f"{a} is lower case")
elif a.isinstance():
    print(f"{a} is alphabetic string")
else:
    print(f"{a} is special character")
