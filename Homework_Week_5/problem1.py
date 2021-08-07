username_and_password = {
    "jack" : "4dm1n@",
    "jill" : "u53r$",
    "peter" : "gu35#"
}

username_and_role = {
    "jack" : "Administrator",
    "jill" : "User",
    "peter" : "Guest"
}

username = input("Username: ")
password = input("Pasword: ")

if username in username_and_password:
    stored_password = username_and_password[username]
    if stored_password == password:
        print(f"Password matched, user role is {username_and_role[username]}.")
    else:
        print("Username or Password didn't match!")
else:
    print("Username or Password didn't match!")