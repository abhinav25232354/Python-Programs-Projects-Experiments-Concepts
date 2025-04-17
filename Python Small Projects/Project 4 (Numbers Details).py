# http://numbersapi.com/number/type

import requests # Requesting for API response

print("\tWelcome to Numbers fact checking")
print("\tNote: This generates random facts from numberapi, and not authentic, please use it for fun only")
print()

while True:
    number = input("\tEnter Number for a Fact: ")
    response = requests.get(f"http://numbersapi.com/{number}")
    print(f"\t{response.text}")