from character.Character import Character

characterName = input("Welke character wil je zijn? ")

c = Character(characterName)

c.showCharacter()
c.showWeapons()

aanval = input("Wil je aanvallen? (y/n)")

if aanval == 'y':
    c.weaponAttack()
