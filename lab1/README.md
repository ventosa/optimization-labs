# Лабораторная работа №1: Линейное программирование

Решение задач ЛП графическим методом и симплекс-методом на Python.

## 📋 Что нужно сделать

1. Реализовать **приведение к канонической форме** (`to_canonical_form`).
2. Реализовать **симплекс-метод** (`simplex_method`).
3. Реализовать **вычисление двойственных переменных** (`get_dual_solution`).
4. Реализовать **сравнение с `scipy.optimize.linprog`** (`solver_scipy.py`).
5. Реализовать **визуализацию** для задач с двумя переменными (`visualize.py`).
6. Убедиться, что все тесты проходят: `pytest tests/ -v`.

## 🚀 Быстрый старт

### 1. Форкните репозиторий

Нажмите кнопку **Fork** в правом верхнем углу на GitHub.

### 2. Клонируйте свой форк

```bash
git clone https://github.com/ВАШ-USERNAME/optimization-labs.git
cd optimization-labs/lab1
```

### 3. Создайте виртуальное окружение

```bash
python -m venv venv
source venv/bin/activate    # Linux/macOS
# или
venv\Scripts\activate       # Windows
```

### 4. Установите зависимости

```bash
pip install -r requirements.txt
```

### 5. Запустите тесты

```bash
pytest tests/ -v
```

Пока функции не реализованы, тесты будут падать с `NotImplementedError` — это нормально.

### 6. Запустите свой вариант

```bash
python main.py --variant 1
```

Без визуализации:

```bash
python main.py --variant 1 --no-plot
```

## ✅ Автоматическая проверка

При каждом `git push` GitHub Actions запускает тесты **только для папки `lab1/`**. Результат смотрите во вкладке **Actions** вашего репозитория.

- 🟢 Зелёная галочка — все тесты прошли.
- 🔴 Красный крестик — есть ошибки, зайдите в лог.

## 📁 Структура папки

```
lab1/
├── data/test_cases.json        # данные тестов
├── tests/                    # тесты (не менять!)
│   ├── test_simplex.py
│   └── test_scipy.py
├── simplex.py                # ← реализовать
├── solver_scipy.py           # ← реализовать
├── visualize.py              # ← реализовать
├── main.py                   # точка входа
├── requirements.txt
└── README.md
```

## ⚠️ Правила

- **Не изменяйте** файлы в `lab1/tests/` — они используются для автопроверки.
- **Не изменяйте** `.github/workflows/lab1.yml`.
- Можно добавлять свои вспомогательные функции и файлы.
- Можно использовать `numpy`, `scipy`, `matplotlib`.

## 📚 Полезные ссылки

- [Симплекс-метод — Википедия](https://ru.wikipedia.org/wiki/Симплекс-метод)
- [scipy.optimize.linprog](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linprog.html)
