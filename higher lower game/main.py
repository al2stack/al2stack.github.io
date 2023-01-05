from game_data import data
from art import logo
from art import vs
import random

print(logo)


#function to generate random item in list
def generate():
    output = random.choice(data)

    name = output["name"]
    description = output["description"]
    country = output["country"]
    followers = output["follower_count"]
    global count
    count.append(followers)
    return f"{name}, a {description}, from {country}"


def same_value(a, b):
    if b == a:
        b = generate()
        same_value(a, b)


#funtion to compare follower count
def compare(user, alternative, count_list):
    global score
    global should_go
    if count_list[user] > count_list[alternative]:
        score += 1
        should_go = True

        print(logo)
        print(f"You got it right, Current Score: {score}")
    else:

        should_go = False
        print(f"That's wrong, Game over! Final Score: {score}")


#global list that contains the 2 follower counts
score = 0
should_go = True
count = []

a = generate()
b = generate()
same_value(a, b)
while should_go:
    print("Choice A: " + a)
    print(vs)
    print("Choice B: " + b)

    choice = input("Who has more followers, A or B? ").lower()
    if choice == "a":
        user_position = 0
        alt = 1
    else:
        user_position = 1
        alt = 0
    compare(user_position, alt, count)
    if should_go == True:
        a = b
        count.remove(count[0])
        b = generate()
