# -- Comparisons --

print(5 == 5)  # True
print(5 > 5)  # False
print(10 != 10)  # False

# Comparisons: ==, !=, >, <, >=, <=

# -- is --
# Python also has the `is` keyword. It's a confusing keyword for now, so I don't recommend using it.

friends = ["Rolf", "Bob"]
abroad = ["Rolf", "Bob"]

print(friends == abroad)  # True
print(friends is abroad)  # False


#explaination: `==` checks for value equality, while `is` checks for reference equality (i.e., whether both variables point to the same object in memory).


#We'll use id() to see how memory works for == and is.

print(id(friends))  # e.g., 140352839123456
print(id(abroad))   # e.g., 140352839123457

# The ids will be different, showing that they are different objects in memory.
# Even though they have the same content, they are different objects in memory that means
# When you create two separate lists, Python stores them in different memory addresses, even if they look identical.
# Therefore, `friends is abroad` evaluates to False.
# In general, use `==` for value comparisons and avoid using `is` unless you specifically need to check for object identity.
# -- in --
friends = ["Rolf", "Bob", "Anne"]
print("Rolf" in friends)  # True
print("Charlie" in friends)  # False
print("Charlie" not in friends)  # True
# -- not --
print(not True)  # False
print(not False)  # True
print(not (5 == 5))  # False
print(not (5 == 6))  # True
print((5 == 5) and (6 > 5))  # True
