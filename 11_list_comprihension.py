###################  1 square
square=[]
for i in range(10):
    square.append(i**2)
print(square)

#list comprehension
squares=[i**2 for i in range(10)]
print(squares)

###################  2 even numbers
even=[]
for i in range(10):
    if i%2==0:
        even.append(i)
print(even)


#list comprehension
evens=[i for i in range(10) if i%2==0]
print(evens)


############ Squares of even numbers

squares_of_even=[i**2 for i in range(10) if i%2==0]
print(squares_of_even)

################## First letter of each word

friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
first_letters= [w[0] for w in friends]

print(first_letters)

################## Length of each word

lengths=[len(w) for w in friends]
print(lengths)

################## Length of each word >3
lengths=[len(w) for w in friends if len(w)>3]
print(lengths)  

#you just spotted the difference between filtering and transforming in list comprehensions.
friends = ["Amy", "John", "Bella", "Raj"]

lengths1 = [len(w) for w in friends if len(w) > 3]
print(lengths1)
# Output: [4, 5]  ? lengths of 'John' and 'Bella'

lengths2 = [w for w in friends if len(w) > 3]
print(lengths2)
# Output: ['John', 'Bella']  ? words themselves


############ Convert to uppercase

upper=[w.upper() for w in friends]
print(upper)

################ Filter strings longer than 5 characters

longer_than_5=[w for w in friends if len(w)>5]
print(longer_than_5)

################ Filter strings that start with 'S'
#no operation just filter '''if w.startswith('S')'''
start_with_s=[w for w in friends if w.startswith('S')]
print(start_with_s)

################ Filter strings that contain 'a'
#no operation just filter '''if 'a' in w'''
contain_a=[w for w in friends if 'a' in w]
print(contain_a)
#output: ['Samantha', 'Saurabh', 'Raj']


################ Filter strings that contain 'a' and convert to uppercase
#operation first then filter '''w.upper()''' then if 'a' in w
contain_a_upper=[w.upper() for w in friends if 'a' in w]
print(contain_a_upper)
#output: ['SAMANTHA', 'SAURABH', 'JEN']


#############Replace negative numbers with 0

numbers = [34, -203, 44, 68, -12, 88, -1]
replaced = [0 if n < 0 else n for n in numbers]
#no_negatives=[n if n>=0 else 0 for n in numbers]
print(replaced)
#output: [34, 0, 44, 68, 0, 88, 0]

#explain
"""For each n in numbers,
if n < 0, use 0,
else use n."""

################ Filter positive numbers and square them
squared_positive=[n**2 for n in numbers if n>0]
print(squared_positive)
#output: [1156, 1936, 4624, 7744]

############Label even/odd

even_odd=["even" if n%2==0 else "odd" for n in numbers]
print(even_odd)
#output: ['even', 'odd', 'even', 'even', 'odd', 'even', 'odd']




############# Nested loops

pairs = []
for i in range(3):
    for j in range(3):
        pairs.append((i, j))
print(pairs)


#list comprehension
pairs = [(i, j) for i in range(3) for j in range(3)]
print(pairs)
#output: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

################ Filtered nested loops
filtered_pairs = [(i, j) for i in range(3) for j in range(3) if i != j]
print(filtered_pairs)
#output: [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]



################# Flatten a matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

flattened = [num for row in matrix for num in row]
print(flattened)        
#output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
#explain
"""
flat = []
for row in matrix:
    for num in row:
        flat.append(num)
First outer loop:

row = [1, 2, 3]

Now the inner loop runs through that row:

num = 1 ? append(1)

num = 2 ? append(2)

num = 3 ? append(3)

? So far: flat = [1, 2, 3]


Second outer loop:

row = [4, 5, 6]

Now the inner loop again runs:

num = 4 ? append(4)

num = 5 ? append(5)

num = 6 ? append(6)

? Final list: flat = [1, 2, 3, 4, 5, 6]
"""


################## Extract keys or values

data = {'a': 10, 'b': 20, 'c': 30}
keys = [k for k in data.keys()]     # ['a', 'b', 'c']
values = [v for v in data.values()] # [10, 20, 30]


########### Filter dictionary items

filtered = {k: v for k, v in data.items() if v > 15}
# {'b': 20, 'c': 30}

#explain
"""
data.items() returns key-value pairs as tuples:

for item in data.items():
    print(item)


Output:

('a', 10)
('b', 20)
('c', 30)


Each tuple = (key, value)

We can unpack it into k and v:

for k, v in data.items():
    print(k, v)


Output:

a 10
b 20
c 30

?? Step 2: Normal for loop (without comprehension)
filtered = {}
for k, v in data.items():
    if v > 15:
        filtered[k] = v


Flow:

Take first item: ('a', 10) ? v = 10 ? 10 > 15? ? ? skip

Take second item: ('b', 20) ? v = 20 ? 20 > 15? ? ? add 'b': 20

Take third item: ('c', 30) ? v = 30 ? 30 > 15? ? ? add 'c': 30

? Final dictionary: {'b': 20, 'c': 30}



###why filtered[k] = v works?

filtered is a dictionary: {} ? currently empty.

k is the key, v is the value.

filtered[k] = v ? stores the value v under the key k.

filtered = {}
k = 'b'
v = 20

filtered[k] = v
print(filtered)
"""



############ Using functions in list comprehensions

def cube(x):
    return x ** 3

cubes = [cube(i) for i in range(5)]
print(cubes)


#output: [0, 1, 8, 27, 64]
#another way

def cube(x): return x ** 3
cubes = [cube(i) for i in range(5)]
print(cubes)

########interview question
#############Remove vowels from a string

def remove_vowels(string):
    vowels = "aeiouAEIOU"
    return ''.join([char for char in string if char not in vowels])

print(remove_vowels("Hello World"))
#output: Hll Wrld

#anotherway
string = "interview"
no_vowels = ''.join([ch for ch in string if ch not in 'aeiou'])

"""
''.join is used to concatenate a list of characters into a single string without any separator.
example of ''.join()
chars = ['H', 'e', 'l', 'l', 'o']
result = ''.join(chars)
print(result)  # Output: Hello

chars = ['Hi', 'there']
result = ' '.join(chars)
print(result)  # Output: Hi there
# include space between Hi and there  
"""


############transpose a matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed = [[row[i] for row in matrix] for i in range(3)]

#explain
"""
# Outer loop iterates over column indices (0, 1, 2)
(0,1,2) are the 3 columns example :  transposed = []
then for i in range(3):  # i is the column index
"""
for i in range(3):
    new_row = []  # Create a new row for the transposed matrix,example: when i=0 then new_row=[]
    # Inner loop iterates over each row in the original matrix
    for row in matrix:
        new_row.append(row[i])  # Append the element at column i to the new row , example: when i=0 then row[0] = 1,4,7
    transposed.append(new_row)  # Append the new row to the transposed matrix , example: [[1,4,7],[2,5,8],[3,6,9]]

    """when is [1,4] appended to transposed?
    when i=0 then new_row=[1,4,7] then transposed.append(new_row) so transposed=[[1,4,7]]
    why its [1,4,7] not [1,4]?
    because new_row collects all elements from the first column of each row.
    when will it be [1,4]?
    it will be [1,4] if the matrix has only two rows instead of three."""
