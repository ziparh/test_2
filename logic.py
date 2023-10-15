from random import randint

import requests

def get_img():
    url = f'https://pokeapi.co/api/v2/pokemon/{randint(1,1000)}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return (data['sprites']['other']['home']['front_default'])
        # Process the response data as needed
    else:
        print('Request failed with status code:', response.status_code)


class Pocemon:

    # Инициализация объекта (конструктор)
    def __init__(self, name):
        self.name = name    # Поле или атрибут класса
        self.img = get_img()

    # Метод класса для получения информации о машине
    def info(self):
        return f"Имя твоего покеомона: {self.name}"
    
    def show_img(self):
        return self.img






