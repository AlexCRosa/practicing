def main():

    # Prompt the user for a number
    number = int(input("Tell me a number: "))

    # Define logic
    def is_prime(number):
        divisor = 2
        while divisor < number:
            if number % divisor == 0:
                return False
            else:
                divisor += 1
                return True

    # Receive logic        
    check = is_prime(number)

    # Decide which message to print
    if check:
        print(f"Number {number} is prime.")
    else:
        print(f"Number {number} is not prime.")

main()

