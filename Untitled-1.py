#1WAP to check number are divisible by 4 and 5 print those numbers 

num1=int(input("enter the no:"))
if num1%4==0 and num1%5==0:
    print(num1,"is divisible by 4 and 5")
else:
    print(num1,"is not divisible by 4 and 5")

#2WAP to determine whether entered angles define a right angled triangle take three values of angle form the user 

anl1=int(input("angle1="))
anl2=int(input("angle2="))
anl3=int(input("angle3="))
if anl1==90 and anl2==90 and anl3==90:
    print("It is not a right angle triangle ")
elif anl1==90 or anl2==60 or anl3==30:
    print("It is a right angle triangle ")
else:
    print("It is not a right angle triangle")

#3Take two number from user and print the sum of those number if the is even

x=int(input("enter the no:"))
y=int(input("enter the no:"))
a=x+y
if a%2==0:
    print(a,"is even")
else:
    print("No output")

#4take a number from the user and check whether it is present in the list its in the list print available

list1=[10,20,30,40,50]
num=int(input("enter the list no:"))
if num%2==0:
    print("Available")
else:
    print("No output")

#5print the core2web string a number of times entered by the user if the number is even

number=int(input("enter the even number:"))
if number%2==0:
    for i in range (number):
        print("core2web")
else:
    print("No output")

#6write a program that checks if a given number is odd using the "if" statement.

num1=int(input("enter the odd and even no:"))
if num1%2==0:
    print("No output")
else:
    print("Odd")

#7Take two number from the user check if both add and then print the sum of the numbers

num1=int(input("enter the no1:"))
num2=int(input("enter the no2:"))
num=num1+num2
if num%2==0:
    print("No output")
else:
    print(num,end=" ")

#8take single character from user check if the ascii value of character is even the print character

char=input("enter the char1=")
if len(char)==1 and ord(char) % 2==0:
    print("char1:",char)
else:
    print("No output")

#9)Take single character from user check if the ascii value both of character are odd then print the sum of ascii value fo character

char1=input("Enter the character:")
char2=input("Enter the character:")
if len(char1)==1 and len(char2)==1 and ord(char1)%2==1 and ord(char2)%2==1:
    ascii_sum = ord(char1)+ord(char2)
    print(ascii_sum,end="")
else:
    print("No output")

#10)Take the number from user modulus with 8 if the remainder of the number is 3 then print reminder.

num=int(input("enter the number:"))
reminder=num % 8
if reminder==3:
    print(reminder,end="")
else:
    print("No output")