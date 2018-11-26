from Chapter1.SetToZero import set_to_zero


def test_set_to_zero():
    arr = [[0, 1, 1], [1, 1, 1], [1, 1, 0]]
    result = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    assert set_to_zero(arr) == result
