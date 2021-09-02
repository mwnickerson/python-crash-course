# Printing Models version 2
# chapter 8
# modifying a list in a function
# previous version but organized to use functions
def print_models(unprinted_designs, completed_designs):
    """
    simulate printing each design until none are left
    move each design to completed when finished
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Currently Printing:{current_design}")
        completed_designs.append(current_design)

def show_completed_models(completed_models):
    """Show all models that were printing"""
    print("\nThe following models are finished printing:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)


