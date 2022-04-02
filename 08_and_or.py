username = "robert"
password = "testpas123"

input_username = input("Username?")
input_password = input("Password?")

if username == input_username and password == input_password:
    print(f"You are logged in {username}")
else:
    print("Username or Password was incorrect")