#!/usr/bin/python3


def fizzbuzz():
    for i in range(0, 101):
        if i != 0:
            if (i % 3) == 0 and (i % 5) == 0:
                i = "FizzBuzz"
            elif (i % 3) == 0:
                i = "Fizz"
            elif (i % 5) == 0:
                i = "Buzz"

            print("{}".format(str(i)), end=' ')
