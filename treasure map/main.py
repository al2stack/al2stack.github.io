
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

float_of_position=str(int(position)/10)
newstring=float_of_position.split(".")
column=int(newstring[0])-1
row=int(newstring[1])-1
map[row][column]="X"



print(f"{row1}\n{row2}\n{row3}")

