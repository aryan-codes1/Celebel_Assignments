#!/usr/bin/env python

def upper_triangle(n: int) -> None:
    for i in range(n):
        for j in range(n):
            if i <= j:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def lower_triangle(n: int) -> None:
    for i in range(n):
        for j in range(n):
            if i >= j:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def pyramid(n: int) -> None:
    for i in range(n):
        for j in range(n-i-1):
            print(end=" ")
        for j in range(i+1):
            print("*", end=" ")
        print()

def inverted_pyramid(n: int) -> None:
    for i in range(n):
        for j in range(i):
            print(end=" ")
        for j in range(n-i):
            print("*", end=" ")
        print()

if __name__ == "__main__":
    n=int(input("Enter the number of rows: "))
    print("Upper Triangle:\n")
    upper_triangle(n)
    print("\nLower Triangle:\n")
    lower_triangle(n)
    print("\nPyramid:\n")
    pyramid(n)
    print("\nInverted Pyramid:\n")
    inverted_pyramid(n)
