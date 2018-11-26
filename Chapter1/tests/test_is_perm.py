from Chapter1.Permutation import is_perm


def test_is_perm():
    assert is_perm('Peter', 'repet')
    assert is_perm('bat', 'tab')
    assert not is_perm('car', 'bar')
