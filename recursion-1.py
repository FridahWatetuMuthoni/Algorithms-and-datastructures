# sum of natural numbers

def sum_natural_numbers(num, sum=0):
    if (num == 0):
        return sum
    return sum_natural_numbers(num - 1, sum + num)


total = sum_natural_numbers(100)
print(total)
