#_my_nwe project
print("Welcome to the accounting school system!")
name = input("Enter your name:")
if name == "gavesh sharma":
    print("Welcome to the system!")
else:
    print("Invalid name . please try agian.")
    exit()

name = input("Enter your name:")

registian_number = input("Enter your registian_number:")

if name == "gavesh" and registian_number == "9528420427":
    print("Welcome to the system!")
elif name == "gavesh" and registian_number != "9528420427":
    print("Incorrect registian_number. please try agian.")
    registian_number = input("Enter your registian_number:")
    if registian_number == "9528420427":
        print("welcome to the system!")
    else:
        print("Beta tumse na ho payga. please try again.")
else:
    print("Invalid name or registian_number. Please try again.")
#_acounting school
main = input('''
1. Totel Fees
2. Fees paid
3. Fees due
4. Thank you for using our syatem\n Sir pls your choice:
             

''')
balence = 10000
if main == "1":
    print("Total Fees:", balence)
    amount = input("Enter the amount you want to pay:")
    if amount >= balence:
        print("Fees paid: ", balence + amount)
elif main == "2":
    print("Fees paid: ", balence + 5000)
elif main == "3":
    print("Fees due: ",balence - 1000) 
elif main == "4":
    print("Thank you for using our system.")
else:
    print("Invalid choice. Please try again.")


