# Sandwiches Vers 2
# chapter 8 exercise 16
# remaking the sandwich maker by importing from modules

import sandwich_function
from sandwich_function import make_sandwich
from sandwich_function import make_sandwich as ms
import sandwich_function as sf
from sandwich_function import *

sandwich_function.make_sandwich('Roast Beef', 'onions', 'mayo', 'spinach')
make_sandwich('Chicken', 'lettuce', 'ketchup')
ms('salami', 'turkey', 'hot sauce', 'olives')
sf.make_sandwich('cheese')