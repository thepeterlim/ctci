def compress_string(text: str) -> str:
    arr = []

    for c in list(text):
        if len(arr) == 0 or arr[len(arr) - 2] != c:
            arr.append(c)
            arr.append(1)
        else:
            arr[len(arr) - 1] = arr[len(arr) - 1] + 1

    result = "".join(map(lambda x: str(x), arr))

    return result if len(result) < len(text) else text
