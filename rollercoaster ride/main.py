print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bil = 0
if height >= 120:
    print("You can ride the rollercoster")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:
        bill = 0
        print("Wish you well in the midlife crisis, you ride free!")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo take? Y or N.")
    if wants_photo == "Y":
        bill += 3
    print(f"Your final bill is ${bill}")
else:
    print("Unfortunately, you can't ride")