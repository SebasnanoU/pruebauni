def sum_number(numbers=None):
    if numbers is None:
        return sum(range(1, 101))
    return sum(numbers)