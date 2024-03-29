# Обчислення визначеного інтеграла методом Монте-Карло

## Опис завдання

В рамках цього завдання було реалізовано програму для обчислення визначеного інтеграла за допомогою методу Монте-Карло. Для порівняння результатів використовувалася функція `quad` з бібліотеки `scipy.integrate`.

## Реалізація алгоритму Монте-Карло

Програма генерує випадкові точки у проміжку [a, b] та обчислює середнє значення функції у цих точках, множене на ширину інтервалу. Кількість випадкових точок може бути змінена за допомогою параметру `num_samples`.

# Висновки щодо правильності розрахунків

Під час виконання домашнього завдання було використано метод Монте-Карло для обчислення визначеного інтеграла функції \(f(x) = x^2\) у проміжку від 0 до 2. Для порівняння результатів використано також функцію `quad` з бібліотеки `scipy.integrate`, яка використовує адаптивний метод квадратур.

Отримані результати:

Точне значення інтеграла: 2.666666666666667

Результат методу Монте-Карло: 2.6729727390894276

Різниця між точним значенням і результатом методу Монте-Карло становить лише 0.006313333333333334, що свідчить про добру точність методу Монте-Карло в даному випадку.

Точність методу Монте-Карло залежить від кількості випадкових вибірок. У цьому експерименті використано 10,000 випадкових точок, що є достатньо для високої точності.

Висновок: Метод Монте-Карло є ефективним інструментом для наближеного обчислення інтегралів, особливо коли аналітичне рішення є складним або неможливим.
