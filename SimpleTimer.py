import time

b = 10 # just change what b equals to edit the time
a = b

response = input("Do you want to start the timer? yes/no \n")
resposne = response.lower()
if response == "yes":
    while True:
        time.sleep(1)
        a -= 1
        print(a)
        if a == 0:
            print(b,"seconds is up")
            break
elif response == "no":
    print("Why did you even run this programme then?!")
else:
    print("Please enter a valid answer!")
