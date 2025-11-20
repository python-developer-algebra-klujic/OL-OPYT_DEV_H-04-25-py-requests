# ZADATAK:
# Pomocu requests biblioteke izdvojite slike jela iz liste recepata
# i pohranite ih u folder "recepti" unutar photos foldera
import requests
import time


URL = 'https://dummyjson.com/recipes'

response = requests.get(URL)

if response.status_code != 200:
    print('Prikazi gresu i prekini izvrsavanje')

recipes = response.json()

for recipe in recipes['recipes']:
    recipe_image = str(recipe['image'])
    file_ext = recipe_image.split('.')[-1]
    recipe_name = str(recipe['name'])
    recipe_name = recipe_name.replace(' ', '_')
    image_response = requests.get(recipe_image)

    with open(f'./photos/recipes/{recipe_name}.{file_ext}', 'wb') as file_writer:
        file_writer.write(image_response.content)

    time.sleep(2)
