import backend as B
from bs4 import BeautifulSoup as bs
import sys

baseURL = 'https://www.pokemon.com'

pokemon = []

descriptions = []

height = []

weight = []

numb = []

img = []

firstPokemon = sys.argv[1]

nextUpName = firstPokemon

nextUpURL = f'/us/pokedex/{firstPokemon}'

looping = True

ii = 0

DEBUG = (False, 5)

while(looping):
    pokemon.append(nextUpName)

    save = B.GrabHTML(f"{baseURL}{nextUpURL}")
    save = bs(save, "html.parser")

    allN = save.findAll("span", {"class": "pokemon-number"})

    numb.append(int(allN[2].text[1:]))
    
    print(numb[-1:][0])

    img.append(f"https://assets.pokemon.com/assets/cms2/img/pokedex/full/{numb[-1:][0]}.png")

    details = save.findAll("span", {"class": "attribute-value"})

    height.append(details[0].text)
    weight.append(details[1].text.split(' ')[0])

    nextUpURL = str(save.find("a", {"class": "next"}, href=True)).split('"')[3]

    nextUpName = save.findAll("span", {"class": "pokemon-name hidden-mobile"})[1].text

    # nextUpName = nextUpName.replace('♀', "-female")
    # nextUpName = nextUpName.replace('♂', "-male")
    # nextUpName = nextUpName.replace("'", "")

    looping = False if nextUpName == firstPokemon else True

    save = save.find("p", {"class": "version-y active"}).text[19:].replace('\n',' ')

    descriptions.append(save)

    if DEBUG[0]:
        ii += 1
        looping = False if ii >= DEBUG[1] else True

print("saving data to tsv...")
with open(f"descriptions.tsv", 'w', encoding='utf8') as f:
    ret = 'index\tname\theight\tweight\tdescription\timage'

    for i in range(len(descriptions)):
        ret += (f"\n{numb[i]}\t{pokemon[i]}\t{height[i]}\t{weight[i]}\t{descriptions[i]}\t{img[i]}")

    f.write(ret)