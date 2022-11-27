salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

money_capital = 0  # количество денег, чтобы прожить 10 месяцев

for nuber in range(0, months):
    balance = abs(salary - spend)
    spend *= 1 + increase
    money_capital += balance

print(round(money_capital))

