"""
Print numbers 1 .. 100
print "Fizz" if divisible by 3
print "Buzz" if divisible by 5
print "FizzBuzz" if divisible by 3 and 5
"""


def fizzBuzz():
    for i in range(1, 100):
        print(i)

        if i % 3 == 0:
            print("Fizz")
        if i % 5 == 0:
            print("Buzz")


if __name__ == "__main__":
    fizzBuzz()
