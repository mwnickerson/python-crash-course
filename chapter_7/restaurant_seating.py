# restaurant seating
# chapter 7 exercise 2
# asks for amount of people and lets them know if its too big

dinner_group = input("How many people are in your dining group? ")
dinner_group = int(dinner_group)
if dinner_group > 8:
    print("Unfortunately, you will have to wait for a table.")
else:
    print(f"We have a table ready for your party of {dinner_group}")