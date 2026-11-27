# row = int(input("enter your row : "))
# col = int(input("enter your col: "))

# for i in range (row):
   # val = ord('A')
#     for j in range(col):
#         print(chr(val),end="")
        
#     print()
#     val+=1



# for i in range (row):
# val = ord('A')
#     for j in range(col): 
#         print(chr(val),end="")
#         val+=1
#         if val>ord('Z'):val=ord('A')
#     print()
  
# val = ord('A')
# for i in range (row):
#     for j in range(col): 
#         print(chr(val),end="")
#         val+=1
#         if val>ord('Z'):val=ord('A')
#     print()
  


# val = ord('A')+row-1
# for i in range (row):
#     for j in range(col): 
#         print(chr(val),end="")
#     print()
#     val-=1
'''output:-
enter your row : 5
enter your col: 5
EEEEE
DDDDD
CCCCC
BBBBB '''


# for i in range (row):
#     val = ord('A')+col-1
#     if val>ord('Z'):val=ord('Z')
#     for j in range(col): 
#         print(chr(val),end=' ')
#         val-=1
#     print()
'''output:- 
enter your row : 5
enter your col: 3
CBA
CBA
CBA
CBA
CBA'''

# for i in range (row):
#     val = col
#     for j in range(col): 
#         print(val,end="")
#         val-=1
#     print()
'''output:- 
enter your row : 4
enter your col: 4
4321
4321
4321
4321
'''
# val=1
# for i in range (row):
#     for j in range(col): 
#         if i%2==0:
#          print(val,end='')
#         else:
#          print('*',end='')
    
#     print()
#     if i%2==0:
#        val+=1
'''output:- 
enter your row : 4
enter your col: 4
1111
****
2222
**** '''



# for i in range (row):
#     val=1
#     for j in range(col): 
#         if j%2==0:
#          print(val,end='')
#          val+=1
#         else:
#          print('*',end='')
    
#     print()
'''output:- 
enter your row : 4
enter your col: 5
1*2*3
1*2*3
1*2*3
1*2*3
'''


# for i in range (row):
#     val=1
#     for j in range(col): 
#         if j%2==0:
#          print(val,end='')
#          val+=1
#         else:
#          print('*',end='')

# 1*2*3
# 4*5*6
# 7*8*9
# 1*2*3
# val=1
# for i in range (row):
#     for j in range(col): 
#         if j%2==0:
#             print(val,end='')
#             val+=1
#             if val>9:val=1    
#         else:
#             print('*',end='')
#     print()

'''output:-
enter your row : 5
enter your col: 5
1*2*3
4*5*6
7*8*9
1*2*3
4*5*6'''





# n= int(input("enter your number : "))
# for i in range (n):
#     for j in range(n):
#         if i>=j: # checking condition for printing * or space
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()

'''output:- 
enter your number : 4
*   
**  
*** 
****
'''


# n= int(input("enter your number : "))
# for i in range (n):
#     for j in range(n):
#         if i<=j: # checking condition for printing * or space
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()

'''output:- enter your number : 4
****
 ***
  **
   *
'''

# n= int(input("enter your number : "))
# for i in range (n):
#     for j in range(n):
#         if i==j: 
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()

'''output:-
enter your number : 5
*    
 *   
  *  
   * 
    *
    '''


# n= int(input("enter your number : "))
# for i in range (n):
#     for j in range(n):
#         if (i+j)==n-1: 
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()

# enter your number : 4
#    *
#   * 
#  *  
# *  

# n= int(input("enter your number : "))
# for i in range (n):
#     for j in range(n):
#         if (i+j)>=n-1: 
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()

# enter your number : 4
#    *
#   **
#  ***
# ****


# n= int(input("enter your number : "))
# for i in range (n):
#     for j in range(n):
#         if (i+j)<=n-1: 
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()

# enter your number : 4
# ****
# *** 
# **  
# *   


# n= int(input("enter your number : "))
# val=1
# for i in range (n):
#     for j in range(n):
#         if i>=j: 
#             print(val,end="")
            
#         else:
#             print(" ",end="")
        
#     print()
#     val+=1

#     enter your number : 4
# 1   
# 22  
# 333 
# 4444


n= int(input("enter your number : "))
val=1
for i in range (n):
    for j in range(n):
        if i>=j: 
            print(val,end="")
            val+=1   
        else:
            print(" ",end="")
        
    print()
    