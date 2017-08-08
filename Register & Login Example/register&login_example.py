print("\nWELCOME...\n")
print("Press Enter for register to the system...")
kayıtbaşlatma = input()
nick = input("Enter your username: ")
ad = input("\nEnter your name :")
soyad = input("\nEnter your surname :")
email = input("\nEnter your e-mail :")
şifre = input("\nEnter your password :")
import time
time.sleep(1)
print("\nRegistration in progress...\n")
time.sleep(1)
print("Registration is completed.\n")
a = 1
while (a > 0):
    print("Press Enter for log in to the system...")
    kayıtbaşlatma = input()
    x = input("Enter your username : ")
    y = input("\nEnter your password : ")
    time.sleep(1)
    if x == nick and y == şifre:
        print("\nLogin in progress...\n")
        time.sleep(1)
        print("Login is completed.\n")
        print("Welcome to the system",ad)
        a = a - 1
    if x != nick and y == şifre:
        time.sleep(1)
        print("\nYour username is incorrect\n")
        print("Please try again...\n")
    if x == nick and y != şifre:
        time.sleep(1)
        print("\nYour password is incorrect\n")
        print("Please try again...\n")
    if x != nick and y != şifre:
        time.sleep(1)
        print("\nYour password and username are incorrect\n")
        print("Please try again...\n")   
    		