from efficiency import has_binary

def test_has_binary_success():
    numbers = [1, 2, 3, 4, 5]
    for i in numbers:
        assert has_binary(i, numbers) is True

def test_has_binary_failure():
    numbers = [1, 2, 3, 4, 5]
    assert has_binary(6, numbers) is False
