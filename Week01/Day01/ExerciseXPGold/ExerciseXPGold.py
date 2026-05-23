#📝 Exercise 1: What is the Season?

#1. Ask the user to input a month (1 to 12).
month = int(input("Enter a month number (1 to 12):"))

summer = range(6,9)
spring = range(3,6)
autumn = range(9,12)

#2. Display the season of the month received:
# - Spring runs from March (3) to May (5)
# - Summer runs from June (6) to August (8)
# - Autumn runs from September (9) to November (11)
# - Winter runs from December (12) to February (2)

if month in spring:
    print("It's Spring!")
elif month in summer:
    print("It's Summer!")
elif month in autumn:
    print("It's Autumn")
elif month == 2 or month ==1 or month == 12:
     print("It's winter!")  
else:
     print("ERROR")
     print("/n Please Enter a month number!")

#📝 Exercise 2: For Loop

nombre = range(1,21)
for i in nombre:
    print(i)

for i in nombre:
    if i % 2 == 0:
     print(i)
    else:
       continue

#📝 Exercise 3: While Loop
name = input("What's your name?: ")
while name != "Olivia":
    print(input("What's your name?: " ) )
    name = input("What's your name?: ")

#📝 Exercise 4: Check the index

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
for i in names:
   a = input("What's your name?: ")
   print(a)
   if a in names:
      index = names.index(a)
      print(index)


#📝 Exercise 5: Greatest Number

First_number = int(input("Entrez un premier nombre: "))
Second_number = int(input("Entrez un second nombre: "))
Third_number = int(input("Entrez un troisième nombre: "))

if First_number >= Second_number and First_number >= Third_number:
   print (f"The greatest number is {First_number}")
elif Second_number >= First_number and Second_number >= Third_number:
   print (f"The greatest number is {Second_number}")
else:
    print (f"The greatest number is {Third_number}")

#📝 Exercise 6: Random number
import random
ask = int(input("Enter a number: "))
nombre_choisi = random.randint(1,10)
if ask == nombre_choisi:
    print("Winner")
else :
   print(f"Better luck next time. The correct number is {nombre_choisi}")