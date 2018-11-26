def is_palindrome_perm(text: str) -> bool:
    d = dict()

    for i in list(text):
        d[i] = d[i] + 1 if i in d else 1

    odd_count = 0

    for k, v in d.items():
        if len(k) > 0 and v % 2 != 0:
            odd_count += 1

    return odd_count > 1
