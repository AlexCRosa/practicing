def fibonacci(x):

    # Defining a list to receive values
    fibonacci_list = [1]

    # Defining a counter to help with the calculation
    counter = 1

    # Loop until the list reaches the amount of elements the user wanted
    while len(fibonacci_list) < x:
        fibonacci_list.append(counter)

        # Fibonacci logic = sum of the two last values
        counter = fibonacci_list[-1] + fibonacci_list[-2]
    return fibonacci_list

amount = int(input("How many numbers to generate? "))

a = fibonacci(amount)

print(a)