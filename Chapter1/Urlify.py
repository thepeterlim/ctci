def urlify(input: str) -> str:
    arr = []
    for c in list(input.strip()):
        if len(c.strip()) == 0:
            arr.append('%20')
        else:
            arr.append(c)
    return "".join(arr)
