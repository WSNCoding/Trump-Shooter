import time

while True:
    print("Welcome to the shop\n")
    time.sleep(2)
    response = input("Do you want to buy or upgrade? upgrade/buy \n")
    response == response.lower()
    if response == "upgrade":
        print("Taking you to the metal store")
    elif response == "buy":
        print("Taking you to the barracks")
    else:
        print("Please enter a valid answer!")
    time.sleep(4)
