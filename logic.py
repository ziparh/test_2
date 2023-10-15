from random import randint

import requests

# Функция для получения рандомной картинки покемона через API
def get_img():
    url = f'https://pokeapi.co/api/v2/pokemon/{randint(1,1000)}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return (data['sprites']['other']['home']['front_default'])
    else:
        get_img()

class Pocemon:

    # Инициализация объекта (конструктор)
    def __init__(self, name):
        self.name = name    # Поле или атрибут класса
        self.img = get_img()

    # Метод класса для получения информации
    def info(self):
        return f"Имя твоего покеомона: {self.name}"

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img






