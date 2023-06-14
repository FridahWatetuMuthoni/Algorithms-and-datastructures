count = 0


def counting_people(n, count):
    if n == 1:
        return count
    count += 1
    return counting_people(n - 1, count)


number_of_people = counting_people(10, count)
print(number_of_people)


def add_all_numbers_to_n(n):
    if (n == 1):
        return 1
    return n + add_all_numbers_to_n(n - 1)


sum = add_all_numbers_to_n(10)
print(sum)


def factorial(n):
    if (n == 1):
        return 1
    return n * factorial(n - 1)


fact = factorial(10)
print(fact)
