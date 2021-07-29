word = input("Enter a word: ")

count = 0

for index in range(0, len(word)):
    if word[index].lower() in ["a", "e", "i", "o", "u"]:
        count = count + 1

if count == 1:
    print(f"'{word}' has {count} vowel!")
else:
    print(f"'{word}' has {count} vowels!")
        