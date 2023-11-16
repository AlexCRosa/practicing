def fibonacci(x):

    # Defining a list to receive values
    counter = 0
    
    # Creating a variable just to store a value
    joker = 0

    # Defining a counter to help with the calculation 
    counter1 = 0
    counter2 = 1

    # Loop until the list reaches the amount of elements the user wanted
    while counter < x:
        counter += 1
        print(counter2, end=" ")

        # Fibonacci logic = sum of the two last values
        joker = counter1

        counter2 = counter1 + counter

    return fibonacci_list

amount_numbers = int(input("How many numbers to generate? "))

a = fibonacci(amount_numbers)

print(a)