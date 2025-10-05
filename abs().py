# memory_diagram_demo.py
# Diagram-style memory explanation for abs(), map(), and list

# -------------------------
# 1️⃣ abs() memory demo
# -------------------------
x = -5
y = abs(x)

# Diagram explanation:
# x ───▶  ┌───────────────┐
#          │ Object: -5    │
#          └───────────────┘
#
# y ───▶  ┌───────────────┐
#          │ Object: 5     │
#          └───────────────┘
#
# Note: abs() creates a new object in memory. Original x remains unchanged.


print("== abs() Memory Demo ==")

a = -42
b = abs(a)

print(f"a = {a}, id(a) = {id(a)}")
print(f"b = abs(a) = {b}, id(b) = {id(b)}")

# -------------------------
# 2️⃣ map() memory demo
# -------------------------
nums = [1, 2, 3, 4]

squares_map = map(lambda x: x**2, nums)

# Diagram explanation:
# nums list: [1, 2, 3, 4] ───▶  ┌─────────┐
#                                   │ Elements stored in memory │
#                                   └─────────┘
#
# squares_map ───▶  ┌──────────────────────────────┐
#                    │ map object: references nums │
#                    │ and function lambda x**2    │
#                    └──────────────────────────────┘
#
# Memory is low because values are calculated "on-the-fly"

print("map() demo:")
for sq in squares_map:
    print(sq)

# -------------------------
# 3️⃣ list() memory demo
# -------------------------
squares_list = [x**2 for x in nums]

# Diagram explanation:
# squares_list ───▶  ┌─────────┐
#                    │ 1       │
#                    │ 4       │
#                    │ 9       │
#                    │ 16      │
#                    └─────────┘
#
# All results stored in memory immediately. Higher memory usage.

print("list() demo:", squares_list)
