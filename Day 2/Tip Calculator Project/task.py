print("welcome to the tip calculator")
bill = int(input("enter the bill: "))
tip = int(input("enter the tip percentage: "))
tip_percentage = tip * 100 / bill
total_bill = bill + tip_percentage
people = int(input("enter the number of people: "))
split = total_bill / people
print(f"each persone shoould pay: ${split}")
