monye_capital = 20000
salary = 5000
spend = 6000
increase = 0.05
count = 0
while monye_capital + salary - spend >= 0:
    monye_capital += salary - spend
    spend += spend * increase
    count += 1
print( "Количество месяцев, которое можно протянуть без долгов:",count)