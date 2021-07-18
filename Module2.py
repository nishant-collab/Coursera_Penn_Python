def getFactors(x):
    """Returns a list of factors of the given number x.
    Basically, finds the numbers between 1 and the given integer that divide the number evenly.

    For example:
    - If we call getFactors(2), we'll get [1, 2] in return
    - If we call getFactors(12), we'll get [1, 2, 3, 4, 6, 12] in return
    """

    # your code here
    factors = []

    # iterate over range from 1 to number x
    for i in range(1, x + 1):

        # check if i divides number x evenly to get factors
        if (x % i == 0):
            factors.append(i)  # add them to factor list

    return factors


def isPrime(x):
    """Returns whether or not the given number x is prime.

    A prime number is a natural number greater than 1 that cannot be formed
    by multiplying two smaller natural numbers.

    For example:
    - Calling isPrime(11) will return True
    - Calling isPrime(71) will return True
    - Calling isPrime(12) will return False
    - Calling isPrime(76) will return False
    """

    factors = []
    for i in range(1, x + 1):  # iterate over a range from 1 to x+1
        if (x % i == 0):  # if the number is divided complelety then add it to list of factors
            factors.append(i)

    length = len(factors)  # finding out length of factors using len function
    if (length == 2):  # checking for number of factors as prime number just have two factors
        return True
    else:
        return False


def isComposite(x):
    """Returns whether or not the given number x is Composite.

    A composite number is a natural number greater than 1 and which has more than two factors

    For example:
    - Calling isComposite(11) will return False
    - Calling isPrime(71) will return True
    - Calling isPrime(12) will return False
    - Calling isPrime(76) will return False
    """

    factors = []
    for i in range(1, x + 1):
        if (x % i == 0):
            factors.append(i)

    length = len(factors)  # finding out length of factors using len function
    if (length > 2):  # checking for number of factors as Composite  number have more than two factors
        return True
    else:
        return False


def isPerfect(x):
    """Returns whether or not the given number x is perfect.

    A number is said to be perfect if it is equal to the sum of all its
    factors (for obvious reasons the list of factors being considered does
    not include the number itself).

    Example: 6 = 3 + 2 + 1, hence 6 is perfect.
    Example: 28 is another example since 1 + 2 + 4 + 7 + 14 is 28.
    Note, the number 1 is not a perfect number.
    """

    factors = []  # first taking an empty list

    # iterate over range from 1 to number x
    for i in range(1, x):  # we dont want to include the number itself so we took the range till x

        # check if i divides number x evenly
        if (x % i == 0):
            factors.append(i)  # add factors of the number to the list 'factors'

    summation = sum(factors)  # add the factors of a number
    if summation == x:  # check if sum of factors is equal to the number
        return True
    else:
        return False


def isAbundant(x):
    """Returns whether or not the given number x is abundant.

    A number is considered to be abundant if the sum of its factors
    (aside from the number) is greater than the number itself.

    Example: 12 is abundant since 1+2+3+4+6 = 16 > 12.
    However, a number like 15, where the sum of the factors.
    is 1 + 3 + 5 = 9 is not abundant.
    """

    factors = []  # first taking an empty list

    # iterate over range from 1 to number x
    for i in range(1, x):  # we dont want to include the number itself so we took the range till x

        # check if i divides number x evenly
        if (x % i == 0):
            factors.append(i)  # add factors of the number to the list 'factors'

    summation = sum(factors)  # add the factors of a number
    if summation > x:  # check if sum of factors is equal to the number
        return True
    else:
        return False


def isTriangular(x):
    """Returns whether or not a given number x is triangular.

    The triangular number Tn is a number that can be represented in the form of a triangular
    grid of points where the first row contains a single element and each subsequent row contains
    one more element than the previous one.

    We can just use the fact that the nth triangular number can be found by using a formula: Tn = n(n + 1) / 2.

    Example: 3 is triangular since 3 = 2(3) / 2
    3 --> 2nd position: (2 * 3 / 2)

    Example: 15 is triangular since 15 = 5(6) / 2
    15 --> 5th position: (5 * 6 / 2)
    """
    # A Triangular number must be
    # sum of first n natural numbers so initially we took sum as 0
    sum, n = 0, 1
    while (sum <= x):  # if sum is less than or equal to given number(x) then execute set of code below

        sum = sum + n  # we add the natural numbers to sum
        if (sum == x):  # if the sum of natural numbers is equal to the number itself then it is triangular
            return True
        n += 1

    return False















def isNarcissistic(x):
    """Returns whether or not a given number is Narcissistic.

    A positive integer is called a narcissistic number if it
    is equal to the sum of its own digits each raised to the
    power of the number of digits.

    Example: 153 is narcissistic because 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153.
    Note that by this definition all single digit numbers are narcissistic.
    """
    return x == sum([int(y) ** len(str(x)) for y in str(x)])# for each digit y in number x, raising it to total number and then adding it

