# 🌟 Exercise : List #1
# Instructions
# Write the following Python code to do the following (complete ALL of these using list comprehension).


#1. Given a list [1,2,3,4], print out all the values in the list.
list = [1, 2, 3, 4]
result = [i for i in list]
print(result)

#2. Given a list [1,2,3,4], print out all the values in the list multiplied by 20.
list = [1, 2, 3, 4]
result = [i * 20 for i in list]
print(result)

#3. Given a list [“Elie”, “Tim”, “Matt”], return a new list with only the first letter ([“E”, “T”, “M”]).
list = ["Elie", "Tim", "Matt"]
result = [i[0] for i in list]
print(result)

#4. Given a list [1,2,3,4,5,6] return a new list of all the even values ([2,4,6]).
list = [1, 2, 3, 4, 5, 6]
result = [i for i in list if i % 2 == 0]
print(result)

#5.Given two lists [1,2,3,4] and [3,4,5,6], return a new list that is the intersection of the two ([3,4]).
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
result = [i for i in list1 if i in list2]
print(result)  

#6.Given a list of words [“Elie”, “Tim”, “Matt”] return a new
#  list with each word reversed and in lower case ([‘eile’, ‘mit’, ‘ttam’]).
list = ["Elie", "Tim", "Matt"]
result = [i[::-1].lower() for i in list]
print(result)

#7. Given two strings “first” and “third”, return a new string with all the letters present in both words ([“i”, “r”, “t”]).
string1 = "first"
string2 = "third"
result = [char for char in string1 if char in string2]
print(result)

#8. For all the numbers between 1 and 100, 
# return a list with all the numbers that are divisible by 12 ([12, 24, 36, 48, 60, 72, 84, 96]).
rangee = range(1, 101)
result = [i for i in rangee if i % 12 == 0]
print(result)

#9. Given the string “amazing”, return a list with all the vowels removed ([‘m’, ‘z’, ‘n’, ‘g’]).
string = "amazing"
vowels = "aeiou"
result = [char for char in string if char not in vowels]
print(result)

#10. Generate a list with the value [[0, 1, 2], [0, 1, 2], [0, 1, 2]].
result = [[i for i in range(3)] for n in range(3)]
print(result)

#11. Generate a list with the value: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9].
result = [[i for i in range(10)] for result in range(10)]
print(result)  