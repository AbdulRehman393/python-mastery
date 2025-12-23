# Variable = A container for a value ( string, integer , float , and boolean)
#            A variable behaves as if it was the value it contains.


first_name = "Abdul"
food = "Burger"
email ="abdul8@example.com"

# Strings = A string is a series of characters , these include number, but we treat them as characters
print(f"Hello {first_name}")   # This is f-string , here f means format, you place your variable inside placeholder {}
print(f"You like {food}")
print(f"Your email is: {email}")

# Integers = Whole numbers
age = 22
quantity = 4
num_of_students = 35

print(f"You are {age} years old")
print(f"You are buying {quantity} items")
print(f"Your class has {num_of_students} students")

# Float = floating point numbers , The term "floating" refers to the decimal point's ability to "float"
price = 18.27
gpa = 3.2
distance = 1.6

print(f"The price is ${price}")
print(f"Your gpa is {gpa}")
print(f"You ran {distance}km")

# Boolean = Either True or False
is_student = True
for_sale  = False
is_online = True

print(f"Are you a student?: {is_student}")

# We will more likely to see the use of Boolean internally with in a program such as woking with if statemnet

if is_student:
    print("You are a student")
else:
    print("You are not a student")

if for_sale:
    print("This item is for sale")
else:
    print("This item is not available")

if is_online:
    print("You are online")
else:
    print("You are offline")
