def is_number_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def is_number_positive(number):
    return number > 0
