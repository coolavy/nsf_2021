palindrome = input("Enter a word: ")

if len(palindrome) > 0:

    palindrome = palindrome.lower()

    if palindrome == palindrome[::-1]:
        print(f"{palindrome} is a palindrome!")
    else:
        print(f"{palindrome} isn't a palindrome!")
else:
    print("Please enter a vaild input.")
