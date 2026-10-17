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


def broken_letter_count(text, letter):
    for character in text:
        count = 0
        if character == letter:
            count += 1
    return count


def broken_score_total():
    total = 0
    while True:
        score = input("Enter a quiz score, or done to finish: ").strip().lower()
        if score == "done":
            break
        total += int(score)
    return total
