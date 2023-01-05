
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


t=name1.count("t")+ name2.count("t")+name1.count("T")+name2.count("T")
r=name1.count("r")+ name2.count("r")+name1.count("R")+name2.count("R")
u=name1.count("u")+name2.count("u")+name1.count("U")+name2.count("U")
e=name1.count("e")+ name2.count("e")+name1.count("E")+name2.count("E")
true=str(t+r+u+e)
l=name1.count("l")+name2.count("l")+name1.count("L")+name2.count("L")
o=name1.count("o")+name2.count("o")+name1.count("O")+name2.count("O")
v=name1.count("v")+name2.count("v")+name1.count("V")+name2.count("V")
e=name1.count("e")+name2.count("e")+name1.count("E")+name2.count("E")
love=str(l+o+v+e)
score=int(true+love)
if score <10 or score>90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score>40 and score <50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")