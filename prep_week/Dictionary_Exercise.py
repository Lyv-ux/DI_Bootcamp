# 🌟 Exercise 1 : Dictionary Exercises
# Instructions
# Write the following Python code to do the following (Complete ALL of the following using dictionary comprehension)


#1. Given a list [("name", "Elie"), ("job", "Instructor")], create a dictionary that looks like this {'job': 'Instructor', 'name': 'Elie'} (the order does not matter).
list_of_tuples = [("name", "Elie"), ("job", "Instructor")]
result = {key: value for key, value in list_of_tuples}
print(result)

#2. Create a dictionary with the key as a vowel in the alphabet and the value as 0. 
# Your dictionary should look like this {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}. (Do not use the fromkeys method).
vowels = 'aeiou'
result = {vowel: 0 for vowel in vowels}
print(result)

#3.Given two lists ["CA", "NJ", "RI"] and ["California", "New Jersey", "Rhode Island"] return a dictionary that looks like this 
# {'CA': 'California', 'NJ': 'New Jersey', 'RI': 'Rhode Island'}. You can research the zip method to help you.
list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]
result = {list1[i]: list2[i] for i in range(0, len(list1))}
print(result)

#4. Create a dictionary starting with the key of the position of the letter and the value
#  as the letter in the alphabet. You should return something like this (Hint - use chr(65) to get the first letter):
result = {i: chr(65 + i) for i in range(27)}
print(result)

#5. Super Bonus
# Given the string “awesome sauce” return a dictionary with 
# the keys as vowels and the values as the count of vowels. Your dictionary should look like {‘a’: 2, ‘e’: 3, ‘i’: 0, ‘o’: 1, ‘u’: 1}
string = "awesome sauce"
vowels = 'aeiou'
result = {vowel: string.count(vowel) for vowel in vowels}
print(result)