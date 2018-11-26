def is_perm(input1: str, input2: str) -> bool:
    d1 = dict()
    d2 = dict()

    for c in list(input1.lower()):
        d1[c] = d1[c] + 1 if c in d1 else 1

    for c in list(input2.lower()):
        d2[c] = d2[c] + 1 if c in d2 else 1

    for k, v in d1.items():
        if k not in d2 or d2[k] != v:
            return False

    return True
