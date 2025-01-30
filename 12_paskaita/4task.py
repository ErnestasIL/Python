def tikrinti_amziu(amzius):
    if amzius < 0:
        raise ValueError('Amzius turi buti teigiamas skaicius')
    if amzius >= 18:
        print('Vartototjas pilnametis!')
    elif amzius < 18:
        print('Vartotojas nepilnametis')

tikrinti_amziu(-5)
tikrinti_amziu(15)
tikrinti_amziu(21)