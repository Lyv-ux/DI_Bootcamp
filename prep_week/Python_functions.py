# 🌟 Exercise 1 : Functions Exercises #1
# Instructions
# Write the following functions



#1. difference

# this function takes in two parameters and returns the difference between the two
# difference(2,2) # 0
# difference(0,2) # -2
def difference(num1, num2):
    return num1 - num2
print(difference(2, 2))  # 0




#2. print_day

# this function takes in one parameter (a number from 1-7) and returns the day of the week (1 is Sunday, 2 is Monday, 3 is Tuesday etc.). If the number is less than 1 or greater than 7, the function should return None
# print_day(4) # "Wednesday"
# print_day(41) # None
def print_day(num):
    days = {
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday"
    }
    return days.get(num, None)
print(print_day(4))  # "Wednesday"
  





#3. last_element

# this function takes in one parameter (a list) and returns the last value in the list. It should return None if the list is empty.
# last_element([1,2,3,4]) # 4
# last_element([]) # None
def last_element(lst):
    if lst:
        return lst[-1]
    return None
print(last_element([1,2,3,4]))  # 4
print(last_element([]))  # None





#4.number_compare

# this function takes in two parameters (both numbers). If the first is greater than the second, this function returns “First is greater.” If the second number is greater than the first, the function returns “Second is greater.” Otherwise the function returns “Numbers are equal.”
# number_compare(1,1) # "Numbers are equal"
# number_compare(1,2) # "Second is greater"
# number_compare(2,1) # "First is greater"
def number_compare(num1, num2):
    if num1 > num2:
        return "First is greater."
    elif num2 > num1:
        return "Second is greater."
    else:
        return "Numbers are equal."
print(number_compare(1, 1))  # "Numbers are equal"





#5.single_letter_count

# this function takes in two parameters (two strings). The first parameter should be a word and the second
#  should be a letter. The function returns the number of times that letter appears in the word. 
# The function should be case insensitive (does not matter if the input is lowercase or uppercase). 
# If the letter is not found in the word, the function should return 0.
# single_letter_count('amazing','A') # 2
def single_letter_count(word, letter):
    word = word.lower()
    letter = letter.lower()
    return word.count(letter)
print(single_letter_count('amazing', 'A'))  # 2



#6.multiple_letter_count

# this function takes in one parameter (a string) and returns a 
# dictionary with the keys being the letters and the values being the count of the letter.
# multiple_letter_count("hello") # {h:1, e: 1, l: 2, o:1}
# multiple_letter_count("person") # {p:1, e: 1, r: 1, s:1, o:1, n:1}
def multiple_letter_count(word):    
    letter_count = {}
    for letter in word:
        letter_count[letter] = letter_count.get(letter, 0) + 1
    return letter_count




#7. list_manipulation

# this function should take in three parameters (a list, command, location and value).

# If the command is “remove” and the location is “end”, the function
#  should remove the last value in the list and return the value removed
# If the command is “remove” and the location is “beginning”,
#  the function should remove the first value in the list and return the value removed
# If the command is “add” and the location is “beginning”,the function should 
# add the value (fourth parameter) to the beginning of the list and return the list
# If the command is “add” and the location is “end”, the function should add the value 
# (fourth parameter) to the end of the list and return the list
# list_manipulation([1,2,3], "remove", "end") # 3
# list_manipulation([1,2,3], "remove", "beginning") # 1
# list_manipulation([1,2,3], "add", "beginning", 20) # [20,1,2,3]
# list_manipulation([1,2,3], "add", "end", 30) # [1,2,3,30]
def list_manipulation(lst, command, location, value=None):
    
    if command == "remove" and location == "end":
        return lst.pop()  

    elif command == "remove" and location == "beginning":
        return lst.pop(0) 
    
    elif command == "add" and location == "beginning":
        lst.insert(0, value) 
        return lst

    elif command == "add" and location == "end":
        lst.append(value) 
        return lst
print(list_manipulation([1, 2, 3], "remove", "end"))       
print(list_manipulation([1, 2, 3], "remove", "beginning"))    
print(list_manipulation([1, 2, 3], "add", "beginning", 20)) 
print(list_manipulation([1, 2, 3], "add", "end", 30))      



#8. is_palindrome

# A Palindrome is a word, phrase, number, or other sequence of characters which reads the same backward or forward. 
# This function should take in one parameter and returns True or False depending on whether it is a palindrome. 
# As a bonus, allow your function to ignore whitespace and capitalization so that is_palindrome('a man a plan a canal Panama') returns True.
# is_palindrome('testing') # False
# is_palindrome('tacocat') # True
# is_palindrome('hannah') # True
# is_palindrome('robert') # False
def is_palindrome(para):
   
    chaine_nettoyee = para.lower().replace(" ", "")
    
    return chaine_nettoyee == chaine_nettoyee[::-1]
print(is_palindrome('testing'))     
print(is_palindrome('tacocat'))   
print(is_palindrome('hannah'))  
print(is_palindrome('robert'))     

print(is_palindrome('a man a plan a canal Panama'))






#9  frequency

# This function accepts a list and a search_term (this will always be a primitive value) and returns the number of times the search_term appears in the list.
# frequency([1,2,3,4,4,4], 4) # 3
# frequency([True, False, True, True], False) # 1
def frequency(lst, search_term):
    compteur = 0
    for element in lst:
        if element == search_term:
            compteur += 1
    return compteur
print(frequency([1, 2, 3, 4, 4, 4], 4))   
print(frequency([True, False, True, True], False)) 
   






#10. flip_case

# This function accepts a string and a letter and reverses the case of all occurances of the letter in the string.
# flip_case("Hardy har har", "h") # "hardy Har Har"
def flip_case(string, letter):
    resultat = []
    
    lettre_cible = letter.lower()
    
    for caractere in string:
        if caractere.lower() == lettre_cible:
            resultat.append(caractere.swapcase())
        else:
            resultat.append(caractere)
            
    return "".join(resultat)
print(flip_case("Hardy har har", "h")) 







#11. multiply_even_numbers

# This function accepts a list of numbers and returns the product of all even numbers in the list.
# multiply_even_numbers([2,3,4,5,6]) # 48
def multiply_even_numbers(lst):
    produit = 1
    a_des_nombres_pairs = False
    
    for nombre in lst:
        # On vérifie si le nombre est pair
        if nombre % 2 == 0:
            produit *= nombre
            a_des_nombres_pairs = True
            
    
    return produit if a_des_nombres_pairs else 0
print(multiply_even_numbers([2, 3, 4, 5, 6]))






#12. mode

# This function accepts a list of numbers and returns the most frequent number in the list of numbers. You can assume that the mode will be unique.
# mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4]) # 4
def mode(lst):
    # max() parcourt les éléments uniques de la liste (grâce à set(lst))
    # et trouve celui qui a le plus grand score selon la fonction lst.count
    return max(set(lst), key=lst.count)
print(mode([2, 4, 1, 2, 3, 3, 4, 4, 5, 4, 4, 6, 4, 6, 7, 4]))





#13. capitalize

# This function accepts a string and returns the same string with the first letter capitalized.
# capitalize("tim") # "Tim"
# capitalize("matt") # "Matt"
def capitalize(string):
    return string.capitalize()
print(capitalize("tim"))
print(capitalize("matt")) 
   




#14. compact

# This function accepts a list and returns a list of values that are truthy values.
# compact([0,1,2,"",[], False, {}, None, "All done"]) # [1,2, "All done"]
def compact(lst):
    # On garde l'élément uniquement si sa valeur de vérité est True
    return [element for element in lst if element]
print(compact([0, 1, 2, "", [], False, {}, None, "All done"]))  






#15. partition

# This function accepts a list and a callback function (which you can assume returns True or False). The function should iterate over each element in the list and invoke the callback function at each iteration. If the result of the callback function is True, the element should go into one list if it’s False, the element should go into another list. When it’s finished, partition should return both lists inside of one larger list.
# def is_even(num):
#     return num % 2 == 0
def partition(lst, callback):
    liste_true = []
    liste_false = []
    
    for element in lst:
        if callback(element):
            liste_true.append(element)
        else:
            liste_false.append(element)
            
    return [liste_true, liste_false]

def is_even(num):
    return num % 2 == 0
print(partition([1, 2, 3, 4], is_even))






#16. intersection

# This function should accept a two dimensional list and return a list with the values that are the same in each list.
# intersection([1,2,3], [2,3,4]) # [2,3]
def intersection(*lists):
    
    if len(lists) == 1 and isinstance(lists[0], list) and isinstance(lists[0][0], list):
        lists = lists[0]
        
    resultat_set = set(lists[0])
    for lst in lists[1:]:
        resultat_set = resultat_set.intersection(set(lst))
        
    return list(resultat_set)
print(intersection([1, 2, 3], [2, 3, 4]))  

print(intersection([[1, 2, 3], [2, 3, 4]])) 





#17. once

# This function accepts a function and returns a new function that can only be invoked once.
#  If the function is invoked more than once, it should return None. Hint you will need 
# to define a new function inside of your once function and return that function. 
# You can add properties to your inner function to see if it has run already.
# def add(a,b):
#     return a + b

# one_addition = once(add)

# one_addition(2,2) # 4
# one_addition(2,2) # undefined
# one_addition(12,200) # undefined
def once(func):
    # Cette variable va mémoriser l'état d'exécution.
    # Grâce au concept de closure, la fonction interne y aura accès.
    deja_execute = False

    def fonction_interne(*args, **kwargs):
        # On utilise le mot-clé 'nonlocal' pour pouvoir modifier la variable 
        # 'deja_execute' située en dehors de cette fonction interne.
        nonlocal deja_execute
        
        if not deja_execute:
            deja_execute = True
            # *args et **kwargs permettent de transmettre n'importe quel 
            # nombre d'arguments à la fonction d'origine (ex: a et b).
            return func(*args, **kwargs)
        else:
            # Si déjà exécutée, on renvoie None (l'équivalent d'undefined en Python)
            return None

    return fonction_interne






#18.  Super bonus
# Research what decorators are and refactor your once code to use a decorator so that you can run

# @run_once
# def add(a,b):
#     return a + b

# add(2,2) # 4
# add(2,20) # None
# add(12,20) # None
from functools import wraps

def run_once(func):
    # Ce dictionnaire ou booléen sert d'état persistant pour la fonction décorée
    deja_execute = False

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal deja_execute
        if not deja_execute:
            deja_execute = True
            return func(*args, **kwargs)
        # Si déjà appelée, renvoie None de manière transparente
        return None

    return wrapper