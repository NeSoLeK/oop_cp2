#Обьявление класса Person
class Person:
    def __init__(self, x):
        self.x = x

    def run(self):
        self.x += 1

# Создаем новый экземпляр человека с начальной позицией 0
kirill = Person(0)

kirill.run()  # Приказываем Кириллу бежать
print(kirill.x)  # Выведет 1
kirill.run()  # Приказываем Кириллу еще раз бежать
print(kirill.x)  # Выведет 2


