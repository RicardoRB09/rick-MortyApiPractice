# # What to do in this task
# Obtén la fecha de emisión del episodio 6 de la cuarta temporada. (tip: El id es 37)
# 1. ¿Qué título tiene ese episodio?
# 2. ¿Cuántos personajes aparecen en ese episodio?
# 3. (plus) Obtén la información completa del 2 personaje que aparece en el listado en orden desc.
#  - nombre
# - especie
# - género
# - estado
# - imagen (si usas jupyter, renderiza la imagen)
# - nombre de su ubicación
# 4. ¿Puedes hacer un collage con 4 imágenes de 4 personajes?


import json, os, requests, sys, random

from urllib.request import urlopen
from PIL import Image
from io import BytesIO

urlCharacters = "https://rickandmortyapi.com/api/character"
urlLocations = "https://rickandmortyapi.com/api/location"  
urlEpisodes = "https://rickandmortyapi.com/api/episode?page=2"

selectedEpisode = {}

def clearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def requestUrl(url):
    response = requests.get(url)
    if response.status_code != 200:
        print('⚠️⚠️ Cannot continue with the execution... Try again! ⚠️⚠️\n')
        sys.exit()
    return json.loads(response.content)



def getAndSaveImageFromUrl(url):
    print('\n⚓ Downloading image... please wait ⚓')

    response = requests.get(url)
    if response.status_code != 200:
        print('⚠️⚠️ Failed to download image!... Try again! ⚠️⚠️\n')
        sys.exit()
    fileName = url.split('/')[-1]
    with open(fileName, 'wb') as file:
        file.write(response.content)
        
    print(f'\n🛤️ Image downloading completed... find it at the directory as {fileName} 🛤️')
   

clearTerminal()

data = requestUrl(urlEpisodes)

# pprint.pprint(data)


# # Searching the 6th episode with id 37
for episode in data['results']:
    if episode['id'] == 37:
        selectedEpisode = episode
        
        

# 0. Obtén la fecha de emisión del episodio 6 de la cuarta temporada. (tip: El id es 37)
print(f'6th episode creation date:  {selectedEpisode['created']}')



# 1. ¿Qué título tiene ese episodio?
print(f'6th episode Title:          {selectedEpisode['name']}')



# 2. ¿Cuántos personajes aparecen en ese episodio?
print(f'6th episode Characters Qty: {len(selectedEpisode['characters'])}')



# 3. (plus) Obtén la información completa del 2 personaje que aparece en el listado en orden desc.
#  - nombre
# - especie
# - género
# - estado
# - imagen (si usas jupyter, renderiza la imagen)
# - nombre de su ubicación
secondCharacterUrl = selectedEpisode['characters'][1]
data = requestUrl(secondCharacterUrl)
print(f'''\n\n💡 Info of the Second Character of the list 💡
📌 Name:      {data['name']}
📌 Specie:    {data['species']}
📌 Gender:    {data['gender']}
📌 Status:    {data['status']}
📌 Image:     {data['image']}
📌 Location:  {data['location']['name']}
''')
getAndSaveImageFromUrl(f'{data['image']}')



# 4. ¿Puedes hacer un collage con 4 imágenes de 4 personajes?
firstCharacterImgUrl = requestUrl(selectedEpisode['characters'][0])['image']
secondCharacterImgUrl = requestUrl(selectedEpisode['characters'][1])['image']
thirdCharacterImgUrl = requestUrl(selectedEpisode['characters'][2])['image']
fourthCharacterImgUrl = requestUrl(selectedEpisode['characters'][3])['image']

getAndSaveImageFromUrl(firstCharacterImgUrl)
getAndSaveImageFromUrl(secondCharacterImgUrl)
getAndSaveImageFromUrl(thirdCharacterImgUrl)
getAndSaveImageFromUrl(fourthCharacterImgUrl)

imagesUrl = [firstCharacterImgUrl, secondCharacterImgUrl, thirdCharacterImgUrl, fourthCharacterImgUrl]

print('\n\n🚨🚨 Creating collage... please wait! 🚨🚨')

images = [Image.open(BytesIO(requests.get(url).content)) for url in imagesUrl]

width, height = images[0].size

collage_width = width * 2
collage_height = height * 2

collage = Image.new('RGB', (collage_width, collage_height))

collage.paste(images[0], (0, 0))
collage.paste(images[1], (width, 0))
collage.paste(images[2], (0, height))
collage.paste(images[3], (width, height))

collage.save('collage.jpeg')

print('\n🛤️ Collage created... find it at the directory as collage.jpeg 🛤️')