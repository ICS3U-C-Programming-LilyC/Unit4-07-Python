#!/usr/bin/env python3

# Created by: Lily Carroll
# Created on: Nov/21/2023
# This program will display the 5 integers per line between numbers 1000 to 2000.


def main():
    # Initiating For loop that will print the integers from 1000 to 2000.
    for counter in range(1000, 2001, 1):
        # If statement inside loop.
        # If the counter is equal to 1000, then print the counter on the same line.
        if counter == 1000:
            print("{} ".format(counter), end="")
        # Elif the counter is divisible by 5 with 0 remainder, then print the counter on the next line.
        elif counter % 5 == 0:
            print("\n{} ".format(counter), end="")
        # Else the counter should be printed on the same line.
        else:
            print("{} ".format(counter), end="")


if __name__ == "__main__":
    main()
