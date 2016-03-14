import time

a = 0
Sure = 0

b = int(input("How many seconds do you want the timer to last for?  "))
a = b


print('Timer set for',b,'seconds.')

Sure = input.lower("Are you sure?  ")
if Sure != "y":
    elif Sure == "n":
        b = int(input("How many seconds do you want the timer to last for?  "))
    else:
        print('Please enter a valid answer')
    

while True:
    response = input("Do you want to start the timer? y/n  ")
    response = response.lower()
    if response == "y":
        print(b or a)
        while True:
            time.sleep(1)
            a -= 1
            print(a)
            if a <= 0:
                print(b,"seconds is up!")
                input('Press enter to exit...')
                break
        break
    elif response == "n":
        print("Why did you even run this program then?!")
    else:
        print("Please enter a valid answer!")
print('Closed program mainloop')
