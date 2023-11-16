def fibonacci(x):

    # Defining a counter to manage user's input
    counter = 0

    # Defining variables to handle the logic of Fibonacci
    num1 = 0
    num2 = 1
    fibonacci_number = num1 + num2

    # Loop until the list reaches the amount of numbers the user wanted
    while counter < x:
        print(fibonacci_number, end=" ")

        # Fibonacci logic = sum of the two previous values
        fibonacci_number = num1 + num2
        num1 = num2
        num2 = fibonacci_number

        counter += 1

amount_numbers = int(input("How many numbers to generate? "))

fibonacci(amount_numbers)