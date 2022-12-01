import pytest

#тестируемая функция
def arifmeticle(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b

print (arifmeticle(4,5,'*'))