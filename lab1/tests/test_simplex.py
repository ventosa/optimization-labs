"""
Тесты для симплекс-метода.

Пока функции содержат raise NotImplementedError,
все тесты будут падать. Это ожидаемо — реализуйте функции
в simplex.py, и тесты начнут проходить.
"""

import pytest
import numpy as np
from simplex import to_canonical_form, simplex_method, get_dual_solution


def test_canonical_form_shapes():
    """Проверка размерностей после приведения к канонической форме."""
    c = [2, 3]
    A = [[1, 2], [3, 1]]
    b = [8, 9]
    signs = ['<=', '<=']
    c_canon, A_canon, b_canon, basis = to_canonical_form(c, A, b, signs, 'max')

    assert c_canon.shape[0] == 4, "Ожидается 4 переменные после канонизации"
    assert A_canon.shape == (2, 4), "Матрица ограничений должна быть 2x4"
    assert len(basis) == 2, "Должно быть 2 базисные переменные"


def test_simplex_variant_1():
    """Вариант 1: max 2x1 + 3x2 при x1+2x2<=8, 3x1+x2<=9."""
    c = [2, 3]
    A = [[1, 2], [3, 1]]
    b = [8, 9]
    signs = ['<=', '<=']

    c_canon, A_canon, b_canon, basis = to_canonical_form(c, A, b, signs, 'max')
    x_opt, obj, history = simplex_method(c_canon, A_canon, b_canon, basis)

    assert np.isclose(obj, 13.0, atol=1e-6), f"Ожидается Z=13, получено {obj}"
    assert np.isclose(x_opt[0], 2.0, atol=1e-6), f"Ожидается x1=2, получено {x_opt[0]}"
    assert np.isclose(x_opt[1], 3.0, atol=1e-6), f"Ожидается x2=3, получено {x_opt[1]}"


def test_simplex_variant_7():
    """Вариант 7: max 5x1 + 3x2 при x1+x2<=6, 2x1+3x2<=14."""
    c = [5, 3]
    A = [[1, 1], [2, 3]]
    b = [6, 14]
    signs = ['<=', '<=']

    c_canon, A_canon, b_canon, basis = to_canonical_form(c, A, b, signs, 'max')
    x_opt, obj, history = simplex_method(c_canon, A_canon, b_canon, basis)

    assert np.isclose(obj, 26.0, atol=1e-6), f"Ожидается Z=26, получено {obj}"


def test_dual_solution():
    """Проверка двойственных переменных для варианта 1."""
    c = [2, 3]
    A = [[1, 2], [3, 1]]
    b = [8, 9]
    signs = ['<=', '<=']

    c_canon, A_canon, b_canon, basis = to_canonical_form(c, A, b, signs, 'max')
    x_opt, obj, history = simplex_method(c_canon, A_canon, b_canon, basis)
    dual = get_dual_solution(np.array(c), np.array(A), np.array(b), basis)

    assert dual.shape == (2,), "Должно быть 2 двойственные переменные"
    assert np.all(dual >= -1e-6), "Двойственные переменные должны быть неотрицательны"
