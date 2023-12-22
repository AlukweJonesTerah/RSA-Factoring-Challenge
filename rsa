#!/usr/bin/python3
"""
1.Factorize as many numbers as possible into a product of two prime numbers.
Usage: factors <file>
    where <file> is a file containing natural numbers to factor.
    One number per line
    You can assume that all lines will be valid natural numbers greater than 1
    You can assume that there will be no empty line, and no space before and after the valid number
    The file will always end with a new line
    Output format: n=p*q
    one factorization per line
    p and q must be prime numbers
See example
You can work on the numbers of the file in the order of your choice
Your program should run without any dependency: You will not be able to install anything on the machine we will run your program on
Time limit: Your program will be killed after 5 seconds if it hasn’t finished
Push all your scripts, source code, etc… to your repository
"""
import sys # gets arguments
def is_prime(num):
    """
    Check if a number is prime."
    :param num: number
    :return: True
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def factorize_rsa(num):
    """
    Function to factorize a number into a product of two prime numbers.
    :param num: kkk
    :return: none
    """
    if num % 2 == 0:
        print("{}={}*{}".format(num, num // 2, 2))
        return

    i = 3
    while i <= num // 2:
        if num % i == 0 and is_prime(i) and is_prime(num // i):
            print("{}={}*{}".format(num, num // i, i))
            return
        i += 2

    # If the loop completes without finding prime factors, print n=n*1
    print("{}={}*{}".format(num, num, 1))


def main():
    """
    Main function to read the file and factorize each number.
    """
    try:
        revfile = sys.argv[1]
        with open(revfile) as f:
            for revnumber in f:
                revnumber = int(revnumber)
                factorize_rsa(revnumber)
    except (IndexError, FileNotFoundError):
        pass


# autostart
if __name__ == "__main__":
    main()
