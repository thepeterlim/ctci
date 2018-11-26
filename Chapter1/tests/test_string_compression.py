from Chapter1.StringCompression import compress_string


def test_compress_string():
    assert compress_string("aabcccccaaa") == "a2b1c5a3"


def test_compress_string_no_compress():
    assert compress_string("abc") == "abc"
