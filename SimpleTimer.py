import time

b = 10 #Use this to set timer not input as this would allow the user interaction
a = b
print('Timer set for',b,'seconds.')
while True:
    response = input("Do you want to start the timer? y/n \n")
    response = response.lower()
    if response == "y":
        print(b or a)
        while True:
            time.sleep(1)
            a -= 1
            print(a)
            if a == 0:
                print(b,"seconds is up!")
                input('Press enter to exit...')
                break
        break
    elif response == "n":
        print("Why did you even run this program then?!")
    else:
        print("Please enter a valid answer!")
print('Closed program mainloop')
