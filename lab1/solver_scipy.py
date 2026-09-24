"""
Решение задач ЛП через scipy.optimize.linprog для сравнения.
"""

from scipy.optimize import linprog
import numpy as np
from typing import List, Tuple, Optional


def solve_with_scipy(
    c: List[float],
    A: List[List[float]],
    b: List[float],
    signs: List[str],
    sense: str = 'max',
    bounds: Optional[List[Tuple[Optional[float], Optional[float]]]] = None
) -> Tuple[np.ndarray, float, bool]:
    """
    Решает задачу ЛП через scipy.optimize.linprog.

    Возвращает:
        x_opt : оптимальное решение
        obj_val : значение целевой функции (в исходной постановке)
        success : флаг успеха
    """
    # TODO: реализовать приведение к виду linprog и вызов
    raise NotImplementedError("Реализуйте solve_with_scipy")
