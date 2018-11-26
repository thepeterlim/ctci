def is_rotation(input1, input2):
    d = []
    for i in range(1, len(input1)):
        d.append(input1[-i:] + input1[0:-i])

    return input2 in d
