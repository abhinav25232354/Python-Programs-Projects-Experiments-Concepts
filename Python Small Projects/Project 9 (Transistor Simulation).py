# Simulating transistor using python code
# Implementing logic gates (Simulation)

# Not Gate
def NOT(n):
    if n==0 or n==1:
        if n==0:
            return 1
        else:
            return 0
    else:
        raise IndexError("Invalid Input: Only 0 and 1 is allowed")

# print(NOT(0))
# print(NOT(1))
# print(NOT(2)) # Raises Error

# OR Gate (Add)
def OR(x, y):
    if (x in [0, 1]) and (y in [0, 1]):
        if x==0 and y==0:
            return 0
        else:
            return 1
    else:
        raise IndexError("Only 0 and 1 allowed") 

# print(OR(0, 0))
# print(OR(0, 1))
# print(OR(1, 0))
# print(OR(1, 1))

# AND Gate (Multiply)
def AND(x, y):
    if (x in [0, 1]) and (y in [0, 1]):
        if x==1 and y==1:
            return 1
        else:
            return 0
    else:
        raise IndexError("Invalid Input: Only 0 and 1 allowed")
    
# print(AND(0, 0))
# print(AND(0, 1))
# print(AND(1, 0))
# print(AND(1, 1))

# NAND Gate (Invert of AND)
def NAND(x, y):
    if (x in [0, 1]) and (y in [0, 1]):
        if x==1 and y==1:
            return NOT(1)
        else:
            return NOT(0)
    else:
        raise IndexError("Invalid Input: Only 0 and 1 allowed")

# print(NAND(0, 0))
# print(NAND(0, 1))
# print(NAND(1, 0))
# print(NAND(1, 1))

# NOR Gate (Invert of OR Gate)
def NOR(x, y):
    if (x in [0, 1]) and (y in [0, 1]):
        if x==0 and y==0:
            return NOT(0)
        else:
            return NOT(1)
    else:
        raise IndexError("Only 0 and 1 allowed") 

# print(NOR(0, 0))
# print(NOR(0, 1))
# print(NOR(1, 0))
# print(NOR(1, 1))

# XOR (Gives 1 if one input is 1)
def XOR(x, y):
    if (x in [0, 1]) and (y in [0, 1]):
        if x!=y:
            return 1
        else:
            return 0
    else:
        raise IndexError("Only 0 and 1 allowed") 

# print(XOR(0, 0))
# print(XOR(0, 1))
# print(XOR(1, 0))
# print(XOR(1, 1))


def XNOR(x, y):
    if (x in [0, 1]) and (y in [0, 1]):
        if x==y:
            return NOT(1)
        else:
            return NOT(0)
    else:
        raise IndexError("Only 0 and 1 allowed") 
    
print(XNOR(0, 0))
print(XNOR(0, 1))
print(XNOR(1, 0))
print(XNOR(1, 1))