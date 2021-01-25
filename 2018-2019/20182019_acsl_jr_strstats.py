import collections

punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

letters = 0
vowels = 0
uppercase = 0

letters_used = []

string = input("Enter a string: ")

#removing punctuation
for element in string:
    if element in punc:
        string = string.replace(element, "")

string_arr = string.split(" ")

for element in string:
    if element == " ":
        string = string.replace(element, "")


for i in range(len(string)):
    curr_string = string[i].lower()
    used = False
    for j in range(len(letters_used)):
        if curr_string == letters_used[j]:
            used = True

    if used == False:
        letters_used.append(curr_string)
        letters += 1

for i in range(len(string)):
    curr_string = string[i].lower()
    if curr_string == "a" or curr_string == "e" or curr_string == "i" or curr_string == "o" or curr_string == "u":
        vowels += 1

for i in range(len(string)):
    if string[i].isupper() == True:
        uppercase += 1

most_freq = collections.Counter(string).most_common(1)[0][1]

longest = max(string_arr, key=len)

print(letters)
print(vowels)
print(uppercase)
print(most_freq)
print(longest)
