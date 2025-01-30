while True:
    ivestis = input('Provide a number: ')
    try:
        res = int(ivestis)
        print(res)
    except ValueError:
        print('huh?')
    else:
        print(f'conversion succesfull: {res}')
    finally:
        print('Program closed...')
    print('-------------------')

