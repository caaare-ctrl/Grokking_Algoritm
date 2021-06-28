# --------------------- Recursion -----------------------
# Think of the base case and recursive case

def countdown(i):
    print(i)
    if i <= 0:
        return
    else:
        countdown(i - 1)


# print(countdown(5))

# --------------- The Stack -------------------------
# like a memo pad push > insert on top
#                 delete > remove the top

# EXAMPLE
def greet(name):
    print("Hello " + name + "!")
    greet2(name)
    print("getting ready to say goodbye")
    bye()


def greet2(name):
    print("how are you, " + name + "?")


def bye():
    print("Goodbye!")


# Call greet("MAGGIE") ---> PRINT("HELLO MAGGIE!")
# --> PUSH greet2("MAGGIE") --> PRINT("HOW ARE YOU ,MAGGIE?)
# --> RETURN TO FUNCTIONAL CALL -> The box on the top of the stack got popped off
# as when you called greet2() , greet() is partially complete state.
# All the values of variable for that are sill stored in memory
# ---> push bye() and call the function print("ok bye!")
# RETURN from the function call --> back to the greet function and there s nth to be done
# so return from the greet function too

# The stack used to save the variables for multiple functions is called call stack


# Recursion Factorial
def factorial(n):
    if n <= 0:
        return 1
    else:
        return n * factorial(n - 1)

# print(factorial(4))

# Saving data in the memory can take up a lot of memory,
# each of function calls takes up some memory,when stack is too tall,
# meaning saving info for many function calls

# You have two options
# 1. Rewrite the code into for loop
# 2. Tail Recursion

