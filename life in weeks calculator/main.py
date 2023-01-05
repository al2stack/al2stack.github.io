
age = input("What is your current age? ")

#calculates total weeks user is alive
time_left=90-int(age)
days_left=time_left*365
weeks_left=time_left*52
months_left=time_left*12
print(f"you have {days_left} days, {weeks_left} weeks, and {months_left} months left")
