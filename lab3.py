#Task 1 (Hailstone Sequence (Collatz Conjecture)

n = int(input("Please enter a positive int greater than 1: "))

while n <= 1:
    n = int(input("Please enter a positive int greater than 1: "))

steps = 0
print(n, end="")

while n != 1:

    if n % 2 == 0:
        n = n // 2
    else:
        n = n * 3 + 1

    print(" ->", n, end="")
    steps += 1

print("\nTotal steps:", steps)
print("Now we are continuing with FızBuzz game. ")

#Task 2 (FizzBuzz Counter)
n = int(input("\nPlease enter a numb between 10 and 100: "))

while n < 10 or n > 100:
    print("Invalid input.")
    n = int(input("Please enter a number between 10 and 100: "))

fizz = 0
buzz = 0
fizzbuzz = 0

for i in range(1, n+1):

    if i % 7 == 0:
        print( i, " is skipped")

    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
        fizzbuzz += 1

    elif i % 3 == 0:
        print("Fizz")
        fizz += 1

    elif i % 5 == 0:
        print("Buzz")
        buzz += 1

    else:
        print(i)


print("Fizz counter: " ,fizz)
print("Buzz counter:" ,buzz)
print("Cızbız counter :" ,fizzbuzz)

#Task 3

n = int(input("Please enter a number between 3 and 9: "))

for i in range(1, 2 * n):
    k = n - abs(n - i)
    
    for j in range(k):
        print("*", end="")

    print()



