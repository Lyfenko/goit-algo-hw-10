from pulp import LpProblem, LpMaximize, LpVariable, lpSum


def optimize_production():
    production_problem = LpProblem("Production_Optimization", LpMaximize)

    lemonade_units = LpVariable("Lemonade_Units", lowBound=0, cat="Integer")
    fruit_juice_units = LpVariable("Fruit_Juice_Units", lowBound=0, cat="Integer")

    water_constraint = 2 * lemonade_units + 1 * fruit_juice_units <= 100
    sugar_constraint = lemonade_units <= 50
    lemon_juice_constraint = lemonade_units <= 30
    fruit_puree_constraint = 2 * fruit_juice_units + 1 * lemonade_units <= 40

    production_problem += water_constraint, "Water_Constraint"
    production_problem += sugar_constraint, "Sugar_Constraint"
    production_problem += lemon_juice_constraint, "Lemon_Juice_Constraint"
    production_problem += fruit_puree_constraint, "Fruit_Puree_Constraint"

    production_problem += lpSum([lemonade_units, fruit_juice_units]), "Total_Production"

    production_problem.solve()

    print("Результат оптимізації виробництва:")
    print(f"Кількість Лимонаду: {lemonade_units.varValue} одиниць")
    print(f"Кількість Фруктового соку: {fruit_juice_units.varValue} одиниць")
    print(
        f"Загальна кількість продуктів: {lemonade_units.varValue + fruit_juice_units.varValue} одиниць"
    )


if __name__ == "__main__":
    optimize_production()
