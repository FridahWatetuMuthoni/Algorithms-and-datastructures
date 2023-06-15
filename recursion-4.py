# converting decimal numbers to binary

num = 233
result = ""


def covert_to_binary(num, result):
    if (num == 0):
        return result

    result = str(num % 2) + result
    return covert_to_binary(num // 2, result)


print(covert_to_binary(num, result))
