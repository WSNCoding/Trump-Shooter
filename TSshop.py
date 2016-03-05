import time

print('Welcome to the shop!')
while True:
    time.sleep(2)
    response = input("Do you want to buy or upgrade? B/U \n")
    response == response.lower()
    if response == "u":
        print("Taking you to the blacksmith...")
        break
    elif response == "b":
        print("Taking you to the barracks...")
        break
    else:
        print("Please enter a valid answer!")
    time.sleep(2)
