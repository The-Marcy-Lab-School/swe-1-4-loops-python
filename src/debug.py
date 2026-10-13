def broken_loop(start, end):
    result = ""
    for i in range(start, end, 2):
        result += str(i)
    return result


def broken_digit_count(text):
    count = 0
    for character in range(len(text)):
        if character.isdigit():
            count += 1
    return count
