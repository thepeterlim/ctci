def is_one_char_away(input1: str, input2: str) -> bool:
    arr1 = [c for c in input1]
    arr2 = [c for c in input2]

    # if the difference is len is greater than 1 will always be false
    if abs(len(arr1) - len(arr2)) > 1:
        return False

    diff_count = 0
    if len(arr1) != len(arr2):
        s_list = arr2 if len(arr2) < len(arr1) else arr1
        l_list = arr2 if len(arr2) > len(arr1) else arr1

        s_index = 0
        l_index = 0

        while s_index < len(s_list):
            if s_list[s_index] != l_list[l_index]:
                diff_count += 1
                if diff_count == 1:
                    l_index += 1
                else:
                    break

            s_index += 1
            l_index += 1

    else:
        index = 0
        while index < len(arr1):
            if arr1[index] != arr2[index]:
                diff_count += 1
            index += 1

    return True if diff_count < 2 else False
