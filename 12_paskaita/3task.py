
while True:
    ivestis = input('Provide a number: ')
    try:
        res = int(ivestis)
        print(res)
    except:
        print('huh?')
    else:
        print(f'conversion succesfull: {res}')
    finally:
        print('Program closed...')
    print('-------------------')

