from problems.median_of_sorted_arrays import medianS


def test_different_len_strings_3():
    result = medianS().findMedianSortedArrays([1, 3], [2])

    assert result == 2


def test_different_len_strings_5():
    result = medianS().findMedianSortedArrays([1, 3, 5], [2, 4])

    assert result == 3


def test_same_len_strings_4():
    result = medianS().findMedianSortedArrays([1, 2], [3, 4])

    assert result == 2.5
