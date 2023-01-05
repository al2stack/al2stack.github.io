
bill=float(input("What was the total bill? $"))
tip=int(input("What percentage tip would you like to give, 10, 12 or 15? "))/100 *bill
total=bill+tip
people=int(input("How many people will split the bill? "))
newbill=total/people
print(f"Each person will pay ${newbill}")