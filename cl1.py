# if condition:
'''  syntax 
if condition :
     statment
    
'''

# ex 
'''
b= int(input("Enter a number: "))
if b==0:
    print("The number is zero")
    '''



''''
a= int(input("Enter a number: "))
if a>0:
    print("hello my boii")

'''


#if else condition:
''' syntax
if condition:
    statement
else:
    statement
'''     


'''
# to check if the number is positive or negative
a= int(input("Enter a number: "))
if a>0:
    print("The number is positive")
else:
    print("The number is negative") 

'''

'''
# wap to check if the number is even or odd
a=int (input("enter your number:    " ))
if a%2==0:
    print("The number is even")
else:
    print("The number is odd")
    '''




'''
# wriet a program to check if the number is divisible by 7 or not
a=int(input("enter your number: "))
if a%7==0:
    print("The number is divisible by 7")
else:
    print("The number is not divisible by 7")
    '''





'''
# write a program to check the number is multiple of 10  or not
a=int(input("enter your number: "))
if a%10==0:
    print("The number is multiple of 10")
else:
    print("The number is not multiple of 10")

    '''


'''
#wap to check enter intger is single digit or not
a= int(input("enter your number: "))
if a>=0 and a<=9:
    print("The number is single digit")
else:
    print("The number is not single digit")


'''

'''
#wap to check enter enteger is two digit or not 
a= int(input("enter your number :"))
#if a>=10 and a<=99 :
# if 10<=a<=99:
if a in range(10,100):
    print("The number is two digit")    
else:
    print("The number is not two digit")
'''

'''
# write a program to check the enter number 3 digit or not
a= int(input("enter your number: "))
if a in range(100,1000):
    print("The number is three digit")
else:
    print("The number is not three digit")

'''

'''
# wap to check enter char is uper case or not 
a= input("enter your char: ")
# if a >= 'A' and a <= 'Z':
#if a.isupper():
if ord(a) in range(65,91):

    print("The char is uper case")
else:
    print("The char is not uper case")
    '''


'''
# write a program to check the enter char is lower case or not
a= input("enter your char: ")
# if a >= 'a' and a <= 'z':
#if a.islower():
if ord(a) in range(97,123):

    print("The char is lower case")
else:
    print("The char is not lower case")
    '''

'''
#wap to check enter char is numric string (0-1) or not
a= input("enter your char: ")
# if a >= '0' and a <= '9':
if ord(a) in range(48,58):
    print("The char is numeric string")
else:
    print("The char is not numeric string")

    '''

'''
#wap to check enter char is vowel or not
a= input("enter your char: ")
if a in ['a','e','i','o','u','A','E','I','O','U']:
    print("The char is vowel")
else:
    print("The char is not vowel")

'''


'''
#wap to check enter char is consonant or not
a= input("enter your char: ")
if  a not in ['a','e','i','o','u','A','E','I','O','U']:
    print("The char is consonant")
else:
    print("The char is not consonant")  

    '''


'''
#wap to check enter value is spacial char or not
a= input("enter your char: ")
#if a in ['!','@','#','$','%','^','&','*','(',')','-','_','=','+','{','}','[',']','|',';',':','"',"'",'<','>',',','.','?','/']:
#if ord(a) in range(33,48) or ord(a) in range(58,65) or ord(a) in range(91,97) or ord(a) in range(123,127):  
if not a.isalnum():   
   print("The char is special char")

else:
    print("The char is not special char")
'''