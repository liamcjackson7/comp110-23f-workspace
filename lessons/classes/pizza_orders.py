from lessons.classes.pizza import Pizza

my_pizza: Pizza = Pizza("large", 10, True)

#my_pizza.size = "large"
#my_pizza.toppings = 10
#my_pizza.gluten_free = True

print("my_pizza: ")
print(my_pizza)

print("Pizza: ")
print(Pizza)

print("Size:")
print(my_pizza.size)

sals_pizza: Pizza = Pizza("medium", 5, False)

def price(input_pizza: Pizza) -> float:
    if input_pizza.size == "large":
        price: float = 6.25
    else:
        price: float = 5.00
    price += 0.75 * input_pizza.toppings
    if input_pizza.gluten_free:
        price += 1.00
    return price