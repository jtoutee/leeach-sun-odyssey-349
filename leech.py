# coding: utf8
import os
import urllib.request
import re
import time
DEBUG = True

url = "http://dicksimonyachts.com/Brochures/Jeanneau/349-Sun-Odyssey/"
directory = "C:/Users/jerom/Dropbox/Python/leech_images_sun_odyssey_349"

# Lire la page
page = urllib.request.urlopen(url).read()

# Tranforme la page de type bytes en type string en la décodant:
page = page.decode("UTF-8")

# Pour chaque .jpg ou .pdf, on va les chercher et on les sauve localement
# <a href="00803e8996f927e84e3fe816615909c8.jpg">
# <a href="Jeanneau-349-Brochure-2016.pdf">

# Transformer la page en liste
liste = re.findall(r'<a href="(.*?)"', page)

# Ne garder que les .jpg et .pdf  (car dans les href on a parfois des r�pertoires ou des .mp4 qu'on ne veut pas
for item in liste:
    if DEBUG: print("item = ", item)
    if (".jpg" not in item) and (".pdf" not in item):
        if DEBUG: print("item pas glop = ", item)
        liste.remove(item)
if DEBUG: print(liste)

# Pour chaque fichier jpg ou pdf, aller le lire puis l'écrire dans directory
for item in liste:
    document_url = url + item   # pas la peine de mettre un "/" car url en avait déjà un à la fin
    if DEBUG: print("document_url =", document_url)
    # On va chercher le contenu du document:
    document = urllib.request.urlopen(document_url).read()
    # On l'écrit dans un fichier du même nom:
    nom_fichier = directory + "/" + item
    if DEBUG: print("nom_fichier =", nom_fichier)
    with open(nom_fichier, 'wb') as fichier:
        fichier.write(document)
    # Ralentir un peu la boucle, sinon le serveur web risque de voir cela comme un DOS
    time.sleep(1)



