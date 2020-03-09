#!/usr/bin/python3
"""
Just a lil program to calulate Fibonacci sequence numbers.

Created by: AUcod3r on 8 March 2020
Why? because I couldn't get the sequence off my mind
after watching the first episode of Devs on Hulu!
"""


def getFib(n):
    """Generate the sequence.

    input one integer greater than 2
    """
    fibSeq = [0, 1]  # First two numbers in the sequence

    for i in range(2, n + 1):
        """Loop to generate a list of the Fibonacci numbers
        starts at 2 and ends with the number input by the user
        """
        fibSeq.append(fibSeq[-1] + fibSeq[-2])

    ratio = fibSeq[-1] / fibSeq[-2]
    """Based on the number input, calulate the ratio of the last 2 numbers
    the higher the input number to generate the sequence,
    the closer the result will be to the golden ratio
    """
    return ','.join(map(str, fibSeq)), ratio  # return the list (as a string
    # list for printing) and the ratio


# Get the number from the user
num = int(input("\nHow many numbers in the Fibonacci sequence do you want to see: "))
seq, ratio = getFib(num)  # store the return into the seq and ratio variables
# Print results:
print(f'\nFibonacci sequence for {num} numbers:', seq, '\n\n'
      f'The golden ratio is 1.61803398875 \nWith {num} numbers, the ratio of the last 2 numbers in the sequence equate to: ', round(ratio, 11))
