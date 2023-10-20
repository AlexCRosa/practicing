string = input("What is the word? ")

if string == string[::-1]:
    print(f"{string.upper()} is a palindrome")