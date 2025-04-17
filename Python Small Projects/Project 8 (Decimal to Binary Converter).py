def decimal_to_binary(n):
    if n == 0:
        return "0"
    binary = ""
    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary  # Prepend the bit
        n = n // 2
    return binary

# Example usage:
decimal = int(input("Enter a decimal number: "))
binary = decimal_to_binary(decimal)
print(f"Binary representation: {binary}")
