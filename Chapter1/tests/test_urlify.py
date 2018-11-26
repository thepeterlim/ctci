from Chapter1.Urlify import urlify


def test_urlify():
    assert urlify("Mr John Smith     ") == r"Mr%20John%20Smith"
