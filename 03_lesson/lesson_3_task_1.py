from user import User

# Создаем экземпляр класса User
my_user = User("Иван", "Курк")

# Вызываем методы и выводим результаты
print(my_user.get_first_name())  # Ожидаемый результат: "Иван"
print(my_user.get_last_name())  # Ожидаемый результат: "Курк"
print(my_user.get_user_info())
# Ожидаемый результат: "User: Иван, last_name: Курк"
