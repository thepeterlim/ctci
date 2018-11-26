from typing import List


def set_to_zero(input_array: List[int]) -> List[int]:
    copy = input_array[:]
    row = []
    col = []

    for r in enumerate(input_array):
        print(f"r:{r}")
        for c in enumerate(r[-1]):
            print(f"c:{c}")
            if c[-1] == 0:
                if r[0] not in row:
                    row.append(r[0])
                if c[0] not in col:
                    col.append(c[0])

    for r in enumerate(copy):
        for c in enumerate(r[-1]):
            if r[0] in row or c[0] in col:
                copy[r[0]][c[0]] = 0

    return copy
