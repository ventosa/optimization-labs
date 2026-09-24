"""
Визуализация задач ЛП с двумя переменными.
"""

import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple, Optional


def plot_feasible_region(
    A: List[List[float]],
    b: List[float],
    signs: List[str],
    bounds: Optional[List[Tuple[float, float]]] = None,
    ax: Optional[plt.Axes] = None
) -> plt.Axes:
    """Строит область допустимых решений для задачи с двумя переменными."""
    # TODO: реализовать построение ОДР
    raise NotImplementedError("Реализуйте plot_feasible_region")


def plot_level_lines(
    c: List[float],
    x_range: Tuple[float, float],
    y_range: Tuple[float, float],
    levels: Optional[List[float]] = None,
    ax: Optional[plt.Axes] = None
) -> plt.Axes:
    """Рисует линии уровня целевой функции."""
    # TODO: реализовать построение линий уровня
    raise NotImplementedError("Реализуйте plot_level_lines")


def plot_gradient(
    c: List[float],
    origin: Tuple[float, float] = (0, 0),
    ax: Optional[plt.Axes] = None,
    **kwargs
) -> plt.Axes:
    """Рисует вектор-градиент целевой функции."""
    # TODO: реализовать построение градиента
    raise NotImplementedError("Реализуйте plot_gradient")


def plot_solution(
    x_opt: Tuple[float, float],
    ax: Optional[plt.Axes] = None,
    **kwargs
) -> plt.Axes:
    """Отмечает оптимальную точку на графике."""
    # TODO: реализовать отметку решения
    raise NotImplementedError("Реализуйте plot_solution")
