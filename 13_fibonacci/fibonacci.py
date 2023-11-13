from operator import length_hint 

amount = int(input("How many numbers to generate? "))

def fibonacci(x):
    fibonacci_sequence = []
    start_number = 1
    while fibonacci_sequence.len() < x:
        fibonacci_sequence.append(start_number)
        start_number += start_number
        return fibonacci_sequence

fibonacci_sequence = fibonacci(amount)

print(fibonacci_sequence)