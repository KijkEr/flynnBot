from helper_functions import read_yaml


class Character:
    def __init__(self, name):
        self.name = name

    char = read_yaml("character.config", "characters.yaml")
