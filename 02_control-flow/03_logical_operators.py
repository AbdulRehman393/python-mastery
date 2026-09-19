# logical operators = used on conditional operators

#                  and = checks two or more conditions if true
#                   or = checks if at least one condition is true
#                  not = True if condition is False, and vice versa

temp = 20
sunny = False
# and
if temp > 0 and temp < 30:
    print("The temperature is good")
else:
    print("The temperature is bad")

# or
if temp <= 0 or temp >= 25:
    print("The temperature is bad")
else:
    print("The temperature is good")

# not
if  not sunny:
    print("It is cloudy outside.")
else:
    print("It is sunny outside.")