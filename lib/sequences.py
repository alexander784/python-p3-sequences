#!/usr/bin/env python3

def print_fibonacci(length):
      if length <= 0:
        print([])
      else:
        a, b = 0, 1
        fib_sequence = [a]
        if length >= 2:
            fib_sequence.append(b)
            for _ in range(2, length):
                c = a + b
                a, b = b, c
                fib_sequence.append(c)
        print(fib_sequence)

print_fibonacci(10)