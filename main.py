def separator(line: str, portion: int = 2):
    """делит строку по N символов"""
    separated = ""
    count = 0

    for char in line:
        separated += char

        count += 1
        if count == portion:
            separated += "|"
            count = 0

    if separated[-1] == "|":
        separated = separated[:-1]
    return separated.split("|")


while True:
    getLine = input("Введите строку: ")

    divide = separator(getLine)
    if len(divide[-1]) == 1:
        divide[-1] += "_"

    print(divide)
