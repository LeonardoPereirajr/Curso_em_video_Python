# Variables...
foods = "bacon, meat, pork chop, landjaeger, hamburger"

# Step00: Just to show the problem...
print("old:\t{0}".format(foods.split(",")))

# Step 01: Split the string and removes the spaces.
food_arr = [food.strip() for food in foods.split(',')]

# Final Step: Printing result...
print("new:\t{0}".format(food_arr))