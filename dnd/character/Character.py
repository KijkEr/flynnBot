from helper_functions import readYaml


class Character():
    def __init__(self, name):
        self.name = name

        self.character = readYaml(
            "character.config", "characters.yaml").get(name)
        self.weapons = readYaml("character.config", "weapons.yaml")

    def showCharacter(self):
        self.characterClass = self.character.get('characterClass')
        self.hitpoints = self.character.get("hitpoints")
        self.race = self.character.get("race")
        self.ac = self.character.get("ac")
        self.level = self.character.get("level")

        print(
            f"{self.name} is een level {self.level} {self.race} {self.characterClass}.")
        print(f"{self.name} heeft {self.hitpoints} hitpoints en {self.ac} ac.")

    def showWeapons(self):
        weapons = self.character.get('weapons')

        print(f"{self.name} heeft de volgende wapens:")

        for key, value in weapons.items():
            print(f"{key}: {value}")
