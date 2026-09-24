"""
Реализация симплекс-метода для решения задач линейного программирования.

реализовать функции, помеченные TODO.
"""

import numpy as np
from typing import List, Tuple


def to_canonical_form(
    c: List[float],
    A: List[List[float]],
    b: List[float],
    signs: List[str],
    sense: str = 'max'
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, List[int]]:
    """
    Приводит задачу ЛП к канонической форме (все ограничения — равенства).

    Параметры:
        c : коэффициенты целевой функции (длина n)
        A : матрица ограничений (m x n)
        b : правая часть ограничений (длина m)
        signs : список знаков ('<=', '>=', '=')
        sense : 'max' или 'min'

    Возвращает:
        c_canon : преобразованные коэффициенты целевой функции
        A_canon : расширенная матрица ограничений (m x N)
        b_canon : правая часть (неотрицательная)
        basis_indices : индексы базисных переменных
    """
    # TODO: реализовать приведение к канонической форме
    raise NotImplementedError("Реализуйте to_canonical_form")


def simplex_method(
    c: np.ndarray,
    A: np.ndarray,
    b: np.ndarray,
    basis: List[int],
    max_iter: int = 1000
) -> Tuple[np.ndarray, float, List[np.ndarray]]:
    """
    Решает задачу ЛП в канонической форме симплекс-методом.

    Возвращает:
        x_opt : оптимальное решение
        obj_val : оптимальное значение целевой функции
        history : список симплекс-таблиц на каждой итерации
    """
    # TODO: реализовать симплекс-метод
    raise NotImplementedError("Реализуйте simplex_method")


def get_dual_solution(
    c: np.ndarray,
    A: np.ndarray,
    b: np.ndarray,
    basis: List[int]
) -> np.ndarray:
    """
    Вычисляет двойственные переменные (теневые цены).
    """
    # TODO: реализовать вычисление двойственных переменных
    raise NotImplementedError("Реализуйте get_dual_solution")
