import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


passwordList = []

for c in range(1, nr_letters + 1):
  passwordList.append(random.choice(letters))

for c in range (1, nr_symbols + 1):
  passwordList.append(random.choice(symbols))

for c in range (1,nr_numbers + 1):
  passwordList.append(random.choice(numbers))

random.shuffle(passwordList)
randomPassword = ""

for c in passwordList:
  randomPassword += c

passwordLenght = len(randomPassword)

print(f"Your random password is '{randomPassword}' ,and your password contains {passwordLenght} characters!")
