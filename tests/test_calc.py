import pytest
from src.calc import factorial

@pytest.fixture()
def get_prime_nums():
    prime_nums = [-1,0,1,14,15,16]
    return prime_nums


def test_fac_lim_values(get_prime_nums):
    nums = get_prime_nums
    assert factorial(nums) == ['ERROR', 1, 1, 87178291200, 1307674368000, 'ERROR']

def test_neg_fac_lim_values(get_prime_nums):
    nums = get_prime_nums
    assert factorial(nums) == ['ERROR', 1, 1, 321321, 1307674368000, 'ERROR']

@pytest.mark.skip(reason='Тестовый пропуск')
def test_fac_lim_values2(get_prime_nums):
    nums = get_prime_nums
    assert factorial(nums) == ['ERROR', 1, 1, 87178291200, 1307674368000, 'ERROR']

@pytest.mark.xfail
def test_neg_fac_lim_values2(get_prime_nums):
    nums = get_prime_nums
    assert factorial(nums) == ['ERROR', 1, 1, 321321, 1307674368000, 'ERROR']

@pytest.mark.mymark
def test_fac():
    nums = []
    assert factorial(nums) == []
