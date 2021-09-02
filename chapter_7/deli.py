# Deli
# chapter 7 exercise 8
# moving sandwich orders from ordered to completed

sandwich_orders = ['tuna fish with mayo', 'spicy meatball sub', \
                   'cheesesteak', 'italian with tomatos', \
                   'roast beef with mustard' ]
finished_orders = []
while sandwich_orders:
    finished_orders = sandwich_orders.pop()

    print(f"Your {finished_orders} sandwich is ready for pickup!")


