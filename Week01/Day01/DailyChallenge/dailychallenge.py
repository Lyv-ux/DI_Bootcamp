#Challenge 1

# 1.Ask the user for a number and a length.
number = int(input("Enter a number: "))
length = int(input("Enter a length: "))

#2. Create a program that prints a list of multiples of the number until the list length reaches length.
for i in range(1, length+1):
    print(number * i)


#Challenge 2
user_word = input("Enter a word: ").strip()
clean_word = ""

for i in range(len(user_word) - 1):
    if user_word[i] != user_word[i + 1]:
        clean_word += user_word[i]

if user_word:
    clean_word += user_word[-1]

print(f"Cleaned word: {clean_word}")