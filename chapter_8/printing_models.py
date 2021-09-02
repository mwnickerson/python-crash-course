# Printing Models
# Chapter 8
# modifying a list in a function
# uses no function

# start with designs that need to be printed
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# simulate printing each one until none are left
# move each design to completed_models after finished
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing: {current_design}")
    completed_models.append(current_design)
# display all completed models
print("\nThe following models have completed printing:")
for completed_model in completed_models:
    print(completed_model)


