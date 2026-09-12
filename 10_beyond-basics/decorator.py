# Decorator = A function that extends the behavior of another function
#             without modifying the base function
#             Pass the base function as an argument as an argument to the decorator


def add_sprinkles(func):
    def wrapper(*args, **kwargs):                  # Now our wrapper function is set to accept any number of arguments and keyword arguments.
        print("You add sprinkles 🧁")              # The wrapper's job is to add extra behavior around the original function.
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):                  # Now our wrapper function is set to accept any number of arguments and keyword arguments.
        print("You add fudge 🍫")                  # The wrapper's job is to add extra behavior around the original function.
        func(*args, **kwargs)
    return wrapper

# We are decorating base function of ice cream with a decorator of add sprinkles, We are not modifying the base function, we are extending it.
@add_sprinkles
@add_fudge                                         # We can apply more than one decorator
def get_ice_cream(flavor):
    print(f"Take your {flavor} icecream🍦")


get_ice_cream("chocolate")


