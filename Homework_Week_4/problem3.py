

words = input("Enter input: ")

words = words.strip()

space_count = 0

for index in range(0, len(words)):
    if words[index] == " " and words[index - 1] != " ":
        space_count = space_count + 1

if space_count > 0:
    number_of_words = space_count + 1
    print(f"'{words}' had {number_of_words} words!")
elif len(words) > 0 and space_count == 0:
    print(f"{words} is 1 word!")
else:
    print("Please enter vaild input.")