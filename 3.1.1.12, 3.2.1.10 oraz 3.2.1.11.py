#3.1.1.12
print("3.1.1.12 \n")
year = int(input("Enter a year: "))

if year<1582:
    print("Not within the Gregorian calendar period")
elif int(year%4)!=0:
    print("Common year")
elif int(year%100)!=0:
    print("Leap year")
elif int(year%400)!=0:
    print("Common year")
else:
    print("Leap year")
    
print("\n")
#3.2.1.10
print("3.2.1.10 \n")
user_word=input("Type the word:")
user_word=user_word.upper()

for letter in user_word:
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        print(letter)

print("\n")
#3.2.1.11
print("3.2.1.11 \n")

word_without_vowels = ""
user_word=input("Type the word:")
user_word=user_word.upper()

for letter in user_word:
    if letter in "AEIOU":
        continue
    word_without_vowels+=letter


print(word_without_vowels)

print("\n")
