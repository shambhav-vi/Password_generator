import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("\n\n\tWelcom to the PyPassword Generator!")
no_letters = int(input("\nHow many letters would you like in your password?\n"))
no_symbols = int(input("How many symbols would you like?\n"))
no_numbers = int(input("How many numbers would you like?\n"))
password = []
for letter in range(1, no_letters+1):
    password += random.choice(letters)

for sym in range(1, no_symbols+1):
    password.append(random.choice(symbols))

for num in range(1, no_numbers+1):
    password.append(random.choice(numbers))

random.shuffle(password)
new_pw = ""
for char in password:
    new_pw += char
print(f"Here is your password : {new_pw}\n")
