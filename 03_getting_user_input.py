# -*- coding: utf-8 -*-
# ================================
# ?? Python User Input Examples
# ================================

# 1. Basic Input (always string)
name = input("Enter your name: ")
print("Hello,", name)
print("Type:", type(name))   # always str

# --------------------------------

# 2. Convert Input to Integer / Float
age = int(input("Enter your age: "))
height = float(input("Enter your height in meters: "))
print("Age:", age, "Height:", height)

# --------------------------------

# 3. Taking Multiple Inputs (same line, space-separated)
x, y = input("Enter two numbers: ").split()
print("x =", x, "y =", y)

# --------------------------------

# 4. Multiple Inputs with Conversion
x, y = map(int, input("Enter two numbers: ").split())
print("Sum =", x + y)

# --------------------------------

# 5. Taking a List of Numbers
nums = list(map(int, input("Enter numbers: ").split()))
print("Numbers List:", nums)

# --------------------------------

# 6. Reading Whole Sentence
sentence = input("Enter a sentence: ")
print("Sentence:", sentence)

# --------------------------------

# 7. Character by Character Input
word = input("Enter a word: ")
for ch in word:
    print(ch)

# --------------------------------

# 8. Input with Custom Separator (comma)
a, b, c = input("Enter values separated by comma: ").split(',')
print("a =", a, "b =", b, "c =", c)

# --------------------------------

# 9. Multiple Lines of Input
print("Enter 3 lines:")
lines = [input() for _ in range(3)]
print("Lines List:", lines)

# --------------------------------

# 10. Using sys.stdin for Fast Input
import sys
print("Enter something (fast input):")
data = sys.stdin.readline().strip()
print("You entered:", data)

# --------------------------------

# 11. Eval Input (?? risky, only for safe inputs)
expr = eval(input("Enter expression: "))
print("Result:", expr)

# ================================
# END OF FILE
# ================================

