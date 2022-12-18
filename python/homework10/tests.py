import functions
import pytest


list_examples = [(6782, 23), (0.56, 11)]


@pytest.mark.parametrize('r, expected', list_examples)
def test_sum_digits(r, expected):
    assert functions.sum_digits(r) == expected


list_examples_err = [('6782', TypeError)]


@pytest.mark.parametrize('r, expected', list_examples_err)
def test_sum_digits_err(r, expected):
    with pytest.raises(expected):
        assert functions.sum_digits(r) == expected


list_examples_2 = [(15, 'yes'), (30, 'no'), (45, 'yes'), (60, 'no')]


@pytest.mark.parametrize('num, expected', list_examples_2)
def test_check_number(num, expected):
    assert functions.check_number(num) == expected

