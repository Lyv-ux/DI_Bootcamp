#Exercise 1: Hello World
print("Hello World\n" * 4)


#Exercise 2: Some Math
result = (99**3)*8
print (result)


#Exercise 3: What is the output?
5 < 3 #False because 5 is superior to 3
3 == 3 #True because it's the same value
3 == "3" #False because the first is a string and the second, an integer
"3" > 3 #False because it isn't the same type
"Hello" == "hello" #False because the first letter is differently written


#Exercise 4: Your computer brand
Computer_brand = "DELL"
print (f"I have a {Computer_brand} computer.")

#Exercise 5: Your information
name = "Olivia"
age = 17
shoe_size = 39
info = (f"My name is {name} I'm {age} years old and my shoe size is {shoe_size}")
print(info)

# Exercise 6: A & B
a = 13
b = 11
if a > b:
    print("Hello World")



#Exercise 7: Odd or Even
nombre = int(input("Entrez un nombre :  "))
if nombre % 2 == 0:
    print("Ceci est un nombre pair")
else:
    print("Ceci est un nombre impair")


# Exercise 8: What’s your name?
my_name = "Olivia"
name_user = str(input("Quel est ton nom? "))
if my_name == name_user:
    print("Yeaahh we have the same name twiin!!!")
else:
    print(f"{name_user}...oh it's a nice name! What does it mean?")


 #Exercise 9: Tall enough to ride a roller coaster
    height_user = int(input("Quelle est votre taille en centimètres? "))
    if height_user > 145:
        print("Tu es assez grand pour monter")
    else:
        print("Tu dois encore grandir un peu pour pouvoir monter")