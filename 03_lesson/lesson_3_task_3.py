from Address import address
from Mailing import mailing


# Создаем объекты класса Address
to_address = Address("1111", "Кунгур", "Центральная", "1", "4")
from_address = Address("2222", "Пермь", "Ленина", "2", "3")
track = Address("3333", "Москва", "Набережая", "3", "2")
cost = Address("4444", "Уфа", "Падерная", "4", "1")

# Создаем объект класса Mailing
Mailing = Mailing(to_address, from_address, track, cost)

# Выводим информацию
print(Mailing)
