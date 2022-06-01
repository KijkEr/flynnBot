from helper_functions import readYaml, calculateAttributeModifier, calculateProficiencyBonus
from character.Character import Character


class Attack(Character):

    def __init__(self, weapon):
        super().__init__(weapon)
        self.attributes = self.character.get("attributes")
        self.attackAttribute = self.character.get("attackAttribute")
        self.level = self.character.get("level")

    def attackAction(self, weapon):
        weapon = self.weapons.get(weapon)
        attributeModifier = calculateAttributeModifier(
            self.attributes.get(self.attackAttribute))
        weaponModifier = weapon.get("modifier")
        profiencyBonus = calculateProficiencyBonus(self.level)
        damageModifier = attributeModifier + weaponModifier

        toHit = weaponModifier + attributeModifier + profiencyBonus

        hitRoll = self.rollToHit(toHit)

        hit = input(f"Raakt {hitRoll}? (y/n): ")

        if hit == "y":
            damageRoll = int(input("Roll damage: "))
            damage = damageRoll + damageModifier
            print(f"Totale damage: {damage}!")

    def rollToHit(self, toHit):
        hitRoll = int(input("Roll to hit: "))
        hitRoll = hitRoll + toHit
        print(f"Totaal to hit: {hitRoll}")
        return hitRoll
