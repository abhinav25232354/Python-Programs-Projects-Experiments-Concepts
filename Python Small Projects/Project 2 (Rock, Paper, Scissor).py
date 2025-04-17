import random

faces = {"r": "Rock", "p":"Paper", "s":"Scissor"}
computer_choice = random.choice([faces["r"], faces["p"], faces["s"]])

user = input("Enter your choice: ")

if user["r"]