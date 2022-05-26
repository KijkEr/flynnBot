def rolePlaying(flynnConfig, sheev):
    stilteTekst = flynnConfig.get('stilteTekst')
    andersTekst = flynnConfig.get('andersTekst')

    stil = input("Is iemand al 10 minuten stil? (y/n): ")
    stil = True if stil == 'y' else False
    if stil:
        print(stilteTekst)

    elif ~stil:
        print(andersTekst)

        sheevInput = input("(y/n): ")
        sheevInput = True if sheevInput == 'y' else False
        if sheev:
            print(sheev)
