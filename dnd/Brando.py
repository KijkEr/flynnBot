from character.Character import Character
from combat.attack import Attack

characterName = "Brando"

a = Attack(characterName)

a.showCharacter()
a.showWeapons()

aanval = input("Wil je aanvallen? (y/n) ")

if aanval == 'y':

    weapon = int(input(
        "Met welk wapen wil je aanvallen? Kies het cijfer dat bij het wapen hoort: "))
    weapon = a.character.get("weapons").get(weapon)
    a.attackAction(weapon)
