import yaml
import os

from styles.flynnCombat import (attack)
from styles.flynnRP import rolePlaying

if __name__ == '__main__':

    cwd = os.getcwd()
    flynnConfigDir = os.path.join(cwd, 'config/')
    with open(os.path.join(flynnConfigDir, 'flynnConfig.yaml')) as file:
        flynnConfig = yaml.safe_load(file)
    with open(os.path.join(flynnConfigDir, 'sheev.txt')) as file:
        sheev = file.read()

    welkomstTekst = flynnConfig.get('welkomstTekst')
    keuze = flynnConfig.get('keuzeTekst')
    print(welkomstTekst)
    mode = input(keuze)

    if mode == 'Combat':
        while True:
            attack()
            stop = input("Is Combat voorbij of ben je dood? (y/n): ")
            stop = True if stop == 'y' else False
            if stop:
                break

    elif mode == 'RP':
        rolePlaying(flynnConfig, sheev)

    else:
        print(f"{mode} is geen keuze. Probeer het opnieuw.")
