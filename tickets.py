ticket = int(input('Укажите количество билетов: '))
price = 0
for i in range(ticket):
    i += 1
    age = int(input(f'Для какого возраста билет №{i}? '))
    if age < 18:
        price += 0
    elif 25 > age >= 18:
        price += 990
    else:
        price += 1390
if ticket > 3:
    print(f'Сумма к оплате {price - ((price / 100) * 10)} руб. с учетом 10%-ой скидки на полную стоимость заказа за регистрацию больше трех человек')
else:
    print(f'Сумма к оплате {price} руб.')