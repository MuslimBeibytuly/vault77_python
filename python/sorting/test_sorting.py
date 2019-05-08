from bubble_sort import bubble_sort
from merge_sort import merge_sort
from selection_sort import selection_sort
def test_bubble_sort():
    l: list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    bubble_sort(l)
    assert l == [17, 20, 26, 31, 44, 54, 55, 77, 93]


def test_merge_sort():
    l: list = [17, 16, 19, 11, 14, 3, 12, 20, 2, 8]
    res = merge_sort(l)
    assert res == [2, 3, 8, 11, 12, 14, 16, 17, 19, 20]

def test_selection_sort():
    l: list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    selection_sort(l)
    assert l == [17, 20, 26, 31, 44, 54, 55, 77, 93]
