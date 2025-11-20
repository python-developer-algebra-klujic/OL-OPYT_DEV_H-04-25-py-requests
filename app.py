import requests
# import json


URL = 'https://dummyjson.com/recipes'

try:
    response = requests.get(URL)
    response.raise_for_status()

    # .content je binary -> odnosno file i koristi se za dohvat slika ili drugih datoteka
    # print(response.content)

    # .text je str i korisitmo ga da bismo sadrzaj konvertirali u dict,
    # odnosno objekt neke klase
    # txt_data = response.text
    # recipes_dict = json.loads(txt_data)
    # print(recipes_dict)
    # for recipe in recipes_dict['recipes']:
    #     print()
    #     print(recipe)
    #     print()

    # kraci nacin gore prikazanog nacina konverzije u dict:
    print()
    print('Nakon koristenja json() metode')
    # .json() metoda je dio requests biblioteke i zato nije potrebno raditi
    # import json standardnog modula
    recipes = response.json()
    for recipe in recipes['recipes']:
        print()
        print(recipe)
        print()



except Exception as ex:
    print(f'Dogodila se greska: {ex}')
