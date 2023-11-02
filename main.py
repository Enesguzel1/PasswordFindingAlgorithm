import random

def faktoriyel(n):
    if n < 0:
        return "Negatif sayıların faktöriyeli tanımsızdır."
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result


def generateUniqueIndexs(repeat, passwordLength, passwordCharacters):
    unique_numbers = set()

    if repeat:
        while len(unique_numbers) < len(passwordCharacters) ** passwordLength:
            password = ''.join(random.choice(passwordCharacters) for _ in range(passwordLength))
            unique_numbers.add(password)
    else:
        while len(unique_numbers) < faktoriyel(passwordLength):
            indices = random.sample(range(len(passwordCharacters)), passwordLength)
            password = ''.join(passwordCharacters[i] for i in indices)
            unique_numbers.add(password)

    return list(unique_numbers)

characters = []
passwordLength = int(input("Şifrenin Uzunluğunu Girin:"))
charactersString = input("Karakter Dizisini Girin: ")
repeat = input("Karakterler Tekrar Ediyor Mu? (True/False)").lower()
characters = list(charactersString)

unique_passwords = generateUniqueIndexs(repeat == "true", passwordLength, characters)

with open("password.txt", "w") as file:
    for password in unique_passwords:
        file.write(password + "\n")


