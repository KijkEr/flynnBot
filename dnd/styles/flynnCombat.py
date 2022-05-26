def attack():
    print('Start van Flynns beurt')

    sa = input('Is Sneak Attack mogelijk? (y/n): ')
    sa = True if sa == 'y' else False

    if sa:
        hitOne = firstAttack()
        secondAttack(hitOne)
    elif ~sa:
        deRest()

    print('Reposition for next round SA.')
    print('Je hebt geen last van opportunity attacks (Swashbuckler).')


def firstAttack():
    damage = '1d8+5, 4d6'
    print('Yes, nuke time bb')
    print('Eduard Triponkie attack (d20 + 8)')

    hit = input('Heeft Flynn zijn tegenstander geraakt? (y/n): ')
    hit = True if hit == 'y' else False
    if hit:
        print('WTF?')
        print(f'Roll damage {damage}')

    return hit


def secondAttack(hitOne):
    if hitOne:
        verplaatsen = input(
            'Wil je dezelfde vijand nog een keer aanvallen? (y/n): ')
        if verplaatsen == 'n':
            print("Verplaats je snel!")
        hit = input('Heeft Flynn zijn tegenstander geraakt? (y/n): ')
        if hit == 'y':
            print('Shank again with dagger (d20+7) (1d4+4)')

    elif ~hitOne:
        print('TWEETRAPS RAKET ATTACK DAGGER (d20+7)')
        hit = input('Heeft Flynn zijn tegenstander geraakt? (y/n): ')
        if hit == 'y':
            print('Beuk die nerd (1d4+4)')


def deRest():
    heal = input("Moet ik iemand healen? (y/n): ")

    if heal == 'y':
        print('Breng het drankje aan op de pijnlijke plek.')

    elif heal == 'n':
        print('FUCK. OPTIMIZER ERROR.')
        print('Throw dagger (d20+7) (1d4+4)')
        print('Bonus action Hide')
