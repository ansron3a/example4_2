import pytest


# тестируемая функция
def arifmeticle(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b
    raise ValueError(f"Неисвестный оператор: {op}")


def test_unknow_op():
    with pytest.raises(ValueError):
        print(arifmeticle(2, 3, '&'))


def test_not_number_val():
    with pytest.raises(TypeError):
        print(arifmeticle(5, 3, '+'))


def test_dew_zero():
    with pytest.raises(ZeroDivisionError):
        print(arifmeticle(3, 0, '/'))


def test_arifm_1():
    assert arifmeticle(3, 4, '*') == 12


def test_arifm_2():
    assert arifmeticle(3, 4, '-') == -1
