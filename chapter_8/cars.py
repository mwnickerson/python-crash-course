# Cars
# Chapter 8 exercise 14
# function that stores dictionary on a car
# Accepts an arbitrary number of features for the cat

def make_car(make, model, **car_info):
    """creates a dictionary to store car info"""
    car_info['car_make'] = make
    car_info['car_model'] = model
    return car_info
car = make_car('Ford', 'Focus SE', color='black',
               tow_package=True)
print(car)

car = make_car('subaru', 'outback', color='blue', tow_package=True)

print(car)
