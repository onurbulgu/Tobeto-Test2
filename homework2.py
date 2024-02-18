# 1- İlk iki elemanı 1'e eşit olan, en az 20 elemanlı bir fibonacci serisini liste halinde oluşturan döngü yazalım.

def fibonacci_series(n):
    fib_series = [1, 1]
    for i in range(2, n):
        fib_series.append(fib_series[i-1] + fib_series[i-2])
    return fib_series

n = 20
fib_series = fibonacci_series(n)
print(f"Fibonacci series with {n} elements: {fib_series}")


# 2- Kullanıcıdan aldığı sayının mükemmel olup olmadığını söyleyen bir program yazınız.(Arş. Mükemmel sayı?)

def is_perfect(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum == n

num = int(input("Enter a number: "))
if is_perfect(num):
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")


# 3- Kullanıcıdan girilen sayının EBOB ve EKOK'unu bulan programı yazınız.
    
number1 = int(input("Enter the first positive integer: "))
number2 = int(input("Enter the second positive integer: "))

def find_gcd(number1, number2):
    while number2:
        number1, number2 = number2, number1 % number2
    return number1

def find_lcm(number1, number2):
    return number1 * number2 // find_gcd(number1, number2)

gcd_result = find_gcd(number1, number2)
lcm_result = find_lcm(number1, number2)

print(f"GCD of entered numbers: {gcd_result}")
print(f"LCM of entered numbers: {lcm_result}")


# 4- Kullanıcıdan girilen sayının asal sayı olup olmadığını söyleyen bir program yazınız.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

# 5- Kullanıcıdan girilen sayının asal çarpanlarını bulan bir program yazınız. 

def prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 2:
        factors.append(n)
    return factors

number = int(input("Enter a number: "))
if number < 2:
    print("Invalid input. Please enter a number greater than or equal to 2.")
else:
    print("Prime factors of", number, "are:", prime_factors(number))