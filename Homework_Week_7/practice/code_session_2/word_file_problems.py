def is_palindrome(word):
    word = word.lower()
    if word == word[::-1]:
        return True
    else:
        return False

# from faker import Faker
# fake = Faker()

# file = open("C:\\Users\\avyan\\python\\nsf_2021\\Homework_Week_7\\practice\\code_session_2\\words.txt", "w")
# for i in range(20):
#     file.write(fake.name() + "\n")
# file.flush()
# file.close()

file_path = "C:\\Users\\avyan\\python\\nsf_2021\\Homework_Week_7\\practice\\code_session_2\\words.txt"

opening_file = open(file_path, "r")

contents = []
palindromes = []

for line in opening_file:
    line = line.strip()
    palindrome = is_palindrome(line)
    if palindrome == True:
        palindromes.append(line)
    contents.append(line)

contents.sort(key=lambda x: len(x))

print(contents)
print("\n")
print(f"Q1:  The longest of {len(contents)} random names is {contents[-1]}")

if not palindromes:
    print("Q2:  There are no palindromes.")
else:
    print(f"Q2:  Palindromes: {palindromes}")