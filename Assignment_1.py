### 1. Data Types and Variables -----------------------------------

# Task 1:
a = 10
b = 20.2
c = "Hello"
d = True

# Task 2:
print("Type of Variable a is: " , type(a))
print("Type of Variable b is: " , type(b))
print("Type of Variable c is: " , type(c))
print("Type of Variable d is: " , type(d))

# Task 3:
add = a + b
print("Addition: ", add)

sub = a - b
print("Subtraction: ", sub)

mul = a * b
print("Multiplication: ", mul)

div = a / b
print("Division: ", div)


print("-"*50)

### 2. Control Flow (if/else) ----------------------------------------------------
# Task 1:
a = int(input("Enter a number: "))

# Task 2:
if(a%2 == 0):
  print("Even Number")
else:
  print("Odd Number")



print("-"*50)

### 3. Strings and Manipulation ----------------------------------------------------

# Task 1:
a = "Hello world"

# Task 2:
print("Upper Case: " , a.upper())
print("Lower Case: " , a.lower())
print("SplitL" , a.split(" "))
print("Length : " , len(a))
print(a.replace("world", "CDIP"))

print("-"*50)

### 4. Loops (for/while) ----------------------------------------------------

# Task 1:
print("Multiply by 2 using for loop")
list1 = [2,3,4,5,6,7,8]
a = len(list1)

for x in range(0,a):
  print(list1[x]/2)

# Task 2:
print("Printing 1 to 10 using while loop")
a = 1
while a<= 10:
  print(a)
  a = a + 1

print("-"*50)

### 5. List & List Comprehension ----------------------------------------------------
# Task 1:
list2 = [ "Banana", "Grapes", "Pineapple", "Orange", "Mango"]
# Task 2:
updatedList = [len(x) for x in list2]
print(updatedList)

# Task 3:
list2.append("Litchi")
print(list2)

# Task 4:
print(sorted(list2))

print("-"*50)


### 6. Dictionary ----------------------------------------------------
# Task 1:
bookdict = {
  "tittle": "Harry Potter and the Philosopher's Stone",
  "author": "J.K. Rowling",
  "year": 1997,
}

# Task 2:
print(bookdict['tittle'])
print(bookdict["author"])
print(bookdict["year"])

# Task 3:
newdict = {
  "genre": "Fantasy",
}

bookdict.update(newdict)
print(bookdict)

# Task 4:
for key, value in bookdict.items():
  print(key, ": " ,value)

print("-"*50)


#Task -- 1 