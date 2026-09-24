"""
Точка входа для запуска лабораторной работы №1.

Использование:
    python main.py --variant 1
    python main.py --variant 1 --no-plot
"""

import argparse
import json
import sys
import numpy as np
import matplotlib

from simplex import to_canonical_form, simplex_method, get_dual_solution
from solver_scipy import solve_with_scipy


def load_variant(filepath: str, variant_id: int) -> dict:
    """Загружает данные варианта из JSON-файла."""
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    if str(variant_id) not in data:
        raise ValueError(f"Вариант {variant_id} не найден в {filepath}")
    return data[str(variant_id)]


def solve_and_compare(variant: dict, plot: bool = True):
    """Решает задачу двумя способами и сравнивает результаты."""
    c = variant['c']
    A = variant['A']
    b = variant['b']
    signs = variant['signs']
    sense = variant['sense']

    # --- Симплекс-метод ---
    c_canon, A_canon, b_canon, basis = to_canonical_form(c, A, b, signs, sense)
    x_simplex, obj_simplex, history = simplex_method(c_canon, A_canon, b_canon, basis)
    dual = get_dual_solution(np.array(c), np.array(A), np.array(b), basis)

    # --- scipy ---
    x_scipy, obj_scipy, success = solve_with_scipy(c, A, b, signs, sense)

    # --- Вывод ---
    print("=" * 55)
    print(f"Вариант {variant.get('id', '?')}")
    print("=" * 55)
    print(f"Целевая функция: {c}, направление: {sense}")
    print()
    print("--- Симплекс-метод ---")
    print(f"  x* = {x_simplex[:len(c)]}")
    print(f"  Z* = {obj_simplex}")
    print(f"  Двойственные переменные: {dual}")
    print()
    print("--- scipy.optimize.linprog ---")
    print(f"  x* = {x_scipy}")
    print(f"  Z* = {obj_scipy}")
    print(f"  success = {success}")
    print()

    if 'expected' in variant:
        exp = variant['expected']
        print("--- Ожидаемый ответ ---")
        print(f"  x* = {exp['x']}, Z* = {exp['obj']}")
        ok_x = np.allclose(x_simplex[:len(c)], exp['x'], atol=1e-4)
        ok_z = np.isclose(obj_simplex, exp['obj'], atol=1e-4)
        print(f"  Совпадение x*: {ok_x}, Z*: {ok_z}")
        print()

    # --- Визуализация ---
    if plot and len(c) == 2:
        try:
            from visualize import (
                plot_feasible_region, plot_level_lines,
                plot_gradient, plot_solution
            )
            fig, ax = plt.subplots(figsize=(8, 8))
            plot_feasible_region(A, b, signs, ax=ax)
            plot_level_lines(c, ax.get_xlim(), ax.get_ylim(), ax=ax)
            plot_gradient(c, ax=ax)
            plot_solution(x_simplex[:2], ax=ax)
            plt.title(f"Вариант {variant.get('id', '?')}: Z* = {obj_simplex:.2f}")
            plt.grid(True, alpha=0.3)
            plt.show()
        except NotImplementedError:
            print("[!] Визуализация не реализована — пропускаем.")


def main():
    parser = argparse.ArgumentParser(description="Лабораторная работа №1: ЛП")
    parser.add_argument('--variant', type=int, required=True, help="Номер варианта")
    parser.add_argument('--data', type=str, default='data/variants.json',
                        help="Путь к файлу с вариантами")
    parser.add_argument('--no-plot', action='store_true', help="Отключить визуализацию")
    args = parser.parse_args()

    if args.no_plot:
        matplotlib.use('Agg')

    variant = load_variant(args.data, args.variant)
    variant['id'] = args.variant
    solve_and_compare(variant, plot=not args.no_plot)


if __name__ == "__main__":
    main()
