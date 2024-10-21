from random import randint

import requests


class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):
        self.health_point = randint(50, 100) 
        self.attack_power = randint(10, 20)

        self.pokemon_number = randint(1, 1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.pokemon_trainer = pokemon_trainer 
        Pokemon.pokemons[pokemon_trainer] = self

    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['other']['official-artwork']['front_default'])
        else:
            return "https://static.wikia.nocookie.net/pokemon/images/0/0d/025Pikachu.png/revision/latest/scale-to-width-down/1000?cb=20181020165701&path-prefix=ru"

    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"


    # Метод класса для получения информации
    def info(self):
        return f"Твой покеомона: {self.name}, hp покемона: {self.health_point}, он атакует с силой: {self.attack_power}"

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img    


    def fight(self, enemy):
        result = []
        result.append(f"Начало боя между {self.name} и {enemy.name}!")
        result.append("")

        while self.is_alive() and enemy.is_alive():
            if isinstance(enemy, Fighter) or isinstance(self, Wizard):
                if isinstance(enemy, Fighter):
                    if randint(1, 4) == 1:
                        result.append(f"{enemy.name} блокирует атаку {self.name}!")
                    elif isinstance(self, Wizard):
                        if randint(1, 2) == 1:
                            super_attack = self.attack_power * 2
                            enemy.health_point -= super_attack
                            result.append(f"{self.name} выпустил огненный шар, у {enemy.name} осталось {enemy.health_point} хп.")
                        else: 
                            enemy.health_point -= self.attack_power
                            result.append(f"{self.name} атакует {enemy.name}, у {enemy.name} осталось {enemy.health_point} хп.")
            else: 
                enemy.health_point -= self.attack_power
                result.append(f"{self.name} атакует {enemy.name}, у {enemy.name} осталось {enemy.health_point} хп.")

            if enemy.is_alive():
                if isinstance(self, Fighter) or isinstance(enemy, Wizard):    
                    if isinstance(self, Fighter):
                        if randint(1, 4) == 1:
                            result.append(f"{self.name} блокирует атаку {enemy.name}!")
                        elif isinstance(enemy, Wizard):
                            if randint(1, 2) == 1:
                                super_attack = enemy.attack_power * 2
                                self.health_point -= super_attack
                                result.append(f"{enemy.name} выпустил огненный шар, у {self.name} осталось {self.health_point} хп.")
                            else: 
                                self.health_point -= enemy.attack_power
                                result.append(f"{enemy.name} атакует {self.name}, у {self.name} осталось {self.health_point} хп.")
                else: 
                    self.health_point -= enemy.attack_power
                    result.append(f"{enemy.name} атакует {self.name}, у {self.name} осталось {self.health_point} хп.")
                    
        if self.is_alive():
             result.append(f"{self.name} побеждает!")
        else:
             result.append(f"{enemy.name} побеждает!")

        return "\n".join(result)

        # while self.is_alive() and enemy.is_alive():
        #     enemy.health_point -= self.attack_power
        #     enemy.health_point = max(enemy.health_point, 0)
        #     result.append(f"{self.name} атакует {enemy.name}, у {enemy.name} осталось {enemy.health_point} хп.")
        #     if enemy.is_alive():
        #         self.health_point -= enemy.attack_power
        #         self.health_point = max(self.health_point, 0)
        #         result.append(f"{enemy.name} атакует {self.name}, у {self.name} осталось {self.health_point} хп.")

        # if self.is_alive():
        #     result.append(f"{self.name} побеждает!")
        # else:
        #     result.append(f"{enemy.name} побеждает!")



        # return "\n".join(result)
        
    def is_alive(self) -> bool:
        if self.health_point > 0:
            return True 
        else:
            return False

class Wizard(Pokemon):
    def __init__(self, pokemon_trainer):
        super().__init__(pokemon_trainer)
        self.health_point = randint(100, 150) 
        self.attack_power = randint(10, 20)


class Fighter(Pokemon):
    def __init__(self, pokemon_trainer):
        super().__init__(pokemon_trainer)
        self.health_point = randint(150, 200)
        self.attack_power = randint(5, 10)


if __name__ == '__main__':
    wizard = Wizard()
    fighter = Fighter()
    print(wizard.info())
    print()
    print(fighter.info())
    print()
    print(fighter.fight(wizard))
    

    