import logging
from abc import ABC, abstractmethod
from math import sqrt
from time import perf_counter
from typing import Callable, Any

from collections import namedtuple

list_1 = [1, 2, 3, 4, 5]
list_2 = [x**2 if x%2==0 else x**4 for x in list_1]
print(list_2)

# Decorator pattern.
# There are two entities to this pattern
# 1. Component - object that has some behaviour (this is the enetey that will be decorated)
# 2. Decorator - object that wraps the Component and adds functionality to it or to another decorator
# Decorators can be stacked. Think onion layers.


# def is_prime(number: int) -> bool:
#     if number < 2:
#         return False
#     for element in range(2, int(sqrt(number)) + 1):
#         if number % element == 0:
#             return False
#     return True

# def test_is_prime():
#     list_of_prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 12]

#     for num in list_of_prime_numbers:
#         if not is_prime(num):
#             print(f"{num} is not prime")


# def benchmark(func):
#     def wrapper(*args: any, **kwargs: any) -> any:
#         logging.info("Benchmark is called")
#         start_time = perf_counter()
#         result = func(*args, **kwargs)
#         end_time = perf_counter()
#         run_time = end_time - start_time
#         logging.info(
#             f"Exectution of {func.__name__} took {run_time:.2f}"
#         )
#         return result
#     return wrapper

# @benchmark
# def count_prime_numbers(upper_bound: int) -> int:
#     logging.info("count_prime_numbers is called")
#     count = 0
#     for num in range(upper_bound):
#         if is_prime(num):
#             count += 1
#     return count

# def main():
#     logging.basicConfig(level=logging.INFO)
#     # func = benchmark(count_prime_numbers)
#     # print(func(10000))
#     print(count_prime_numbers(10000))

# if __name__ == "__main__":
#     main()


    #logging.info(f"There are {value} prime numbers")
