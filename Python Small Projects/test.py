# (a+b)^2
# Automating Mathematical Formula with python
try:
    a = int(input("Enter A: "))
    b = int(input("Enter B: "))
    print(f"{a}+{b}^2")
    z = a**2 + 2*(a*b) + b**2
    print(z)
except Exception as e:
    print(e)