#_my_nwe project
name = input("Enter your name:")

password = input("Enter your password:")

if name == "gavesh" and password == "12345":
    print("Welcome to the system!")
elif name == "gavesh" and password != "12345":
    print("Incorrect password. please try agian.")
    password = input("Enter your password:")
    if password == "12345":
        print("welcome to the system!")
    else:
        print("Beta tumse na ho payga. please try again.")
else:
    print("Invalid name or password. Please try again.")
