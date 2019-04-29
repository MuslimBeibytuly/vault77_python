from bubble_sort import bubble_sort
from merge_sort import merge_sort
def test_bubble_sort():
    l: list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    bubble_sort(l)
    assert l == [17, 20, 26, 31, 44, 54, 55, 77, 93]


def test_merge_sort():
    l: list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    merge_sort(l)
    assert l == [17, 20, 26, 31, 44, 54, 55, 77, 93]
