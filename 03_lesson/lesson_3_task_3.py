from address import Address
from mailing import Mailing


# Создаем объекты класса Address
to_address = Address("1111", "Кунгур", "Центральная", "1", "4")
from_address = Address("2222", "Пермь", "Ленина", "2", "3")


# Создаем объект класса Mailing
Mailing = Mailing(to_address, from_address, 333, "TRK666666")

# Выводим информацию
print(Mailing)
