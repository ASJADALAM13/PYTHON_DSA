#1.
def pyramid(n1):
    for i in range(n1):

        for j in range(n1-i+1):
            print(" ",end=" ")
        
        for star in range((2*i)+1):
            print("*",end=" ")

        print(" ")
"""
pyramid(5)
            *  
          * * *
        * * * * *
      * * * * * * *
    * * * * * * * * *
    """

#2.
def upside_down_pyramid(n2):
    for i in range(n2,-1,-1):
        for j in range(n2-i+1):
            print(" ",end=" ")

        for star in range(2*i+1):
            print("*",end=" ")
        
            
        print(" ")
"""
upside_down_pyramid(5)
  * * * * * * * * * * *  
    * * * * * * * * *
      * * * * * * *
        * * * * *
          * * *
            *
""" 
#3.
def diamond(n3):
    pyramid(n3)           # IF i merge the code of  method Pyramid and upside_down_pyramid i will get a diamond
    upside_down_pyramid(n3)

"""
diamond(5)
            *  
          * * *
        * * * * *
      * * * * * * *
    * * * * * * * * *
  * * * * * * * * * * *
    * * * * * * * * *
      * * * * * * *
        * * * * *
          * * *
            *  
"""
#4.
def  half_diamond(n4):
    for i in range(n4):
        for j in range(i+1):
            print("*",end=" ")
        print(" ")

    for i in range(n4-1,0,-1):
        for j in range(i):
            print("*",end=" ")
        print(" ")
"""
half_diamond(5)
*  
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""

#5.
def binary_right_angled_triangle(n5):
    start_var=1
    for i in range(n5):
        if i%2==0:
            start_var=0
        else:
            start_var=1

        for j in range(i):
            print(start_var,end=" ")
            start_var=1-start_var
        print(" ")
"""
binary_right_angled_triangle(5)

1  
0 1  
1 0 1  
0 1 0 1  """

#6.
def logical_num_pattern(n6):
    for i in range(n6):
        for j in range(i+1):
            print(j+1,end="")
            
        for k in range((2*n6)-(2*(i+1))):
            print(" ",end="")    

        for l in range(i+1,0,-1):
            print(l,end="")

        print(" ")

"""       
logical_num_pattern(4)

1      1 
12    21 
123  321 
12344321 """

#7.
def logical_num_upto(n7):
    num=1
    for i in range(n7):
        for j in range(i):
            print(num,end=" ")
            num=num+1
        print("")
"""
logical_num_upto(6)

1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 """


#8.
def alpha_pattern(str,n8):
    for i in range(n8+1):
        for j in range(i):
            print(str[j],end="")

        print(" ")
"""
str=input("Enter:") #ABCDE
alpha_pattern(str,len(str))

->
A
AB
ABC
ABCD
ABCDE"""

#9.
def rev_alpha_pattern(str,n9):
    for i in range(n9):
        for j in range(n9-i):
            print(str[j],end="")

        print(" ")  
""""   
str=input("Enter:")   #ABCDE
rev_alpha_pattern(str,len(str))
->
ABCDE 
ABCD 
ABC 
AB 
A 
"""

#10.
def alpha_pattern_2(str,n1a):
    for  i in range(n1a+1):
        for j in range(i):
            print(str[i-1],end="")
        print(" ")
"""
str=input("Enter:")   #ABCDE       
alpha_pattern_2(str,len(str))

A
BB
CCC
DDDD
EEEEE

"""
#11.

def alpha_pyramid(str,n11):

    for i in range(n11):
        for j in range(n11-i+1):
            print(" ",end=" ")

        for k in range((2*i+1)):
            print(str[i],end=" ")


        print(" ")
            
"""
alpha_pyramid("ABCDE",5)
           
            A
          B B B
        C C C C C
      D D D D D D D
    E E E E E E E E E

"""