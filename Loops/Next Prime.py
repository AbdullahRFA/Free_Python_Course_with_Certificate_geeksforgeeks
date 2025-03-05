
"""
Given an integer n. Write a program to find the first prime number greater than n.

Examples:

Input: n = 15
Output: 17
Explanation: 17 is next prime number.
Input: n = 7
Output: 11
Explanation: 11 is the prime number next to 7.
"""
def is_prime(num):
    check = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            check = False
            break
    return check


def next_prime(n):
    num = n + 1
    while True:
        if is_prime(num):
            return num
        num += 1


n = int(input())
print(next_prime(n))
