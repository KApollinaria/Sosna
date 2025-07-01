from smartphone import Smartphone

# Создаем список абонентских номеров (контакты)
catalog = [
    Smartphone("Apple", "iPhone", "+79001112231"),
    Smartphone("HONOR", "X9c", "+79004445562"),
    Smartphone("Redmi", "Note", "+79007778893"),
    Smartphone("Samsung", "gelaxy", "+7900162234"),
    Smartphone("POCO", "F7", "+79002717235"),
]

# Печатаем контакты
for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model} - {smartphone.number}")
