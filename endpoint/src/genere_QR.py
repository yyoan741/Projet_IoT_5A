import qrcode
from PIL import Image
import requests
import json
import random
import string
import time

#debut mesure du temps d execution
begin= time.time()

#Fonction de Génération d une chaîne aléatoire de longueur fixe
def random_string(len):

    str = string.ascii_lowercase
    return ''.join(random.choice(str) for i in range(len))

#on genere une chaine de caractere aleatoire de 1000 caracteres
rand_cle = random_string(1000)

#on cryptypte cette chaine et on genere un QRcode
rand_cle_crypt=str(hash(rand_cle))
QR_code=qrcode.make(rand_cle_crypt)

#on l affiche et on le sauvegarde dans un fichier
print(QR_code)
QR_code.save('QR_CODE_PORTE_crypt.jpg')

#mesure fin du temps d execution
end= time.time()

#affichage temps d execution du programme
print("temps d'execuction : {} s".format(end-begin))

#Ancien code pour envoyer des données su rl'ancien API du serveur homeassistant
'''url = "http://localhost:8123/api/events/"
api_token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiI4MGY0NWE4OTJhNzI0M2QzYjFiYzI1ZTdkOTE3NTVmNyIsImlhdCI6MTY3MTAwNDM3NiwiZXhwIjoxOTg2MzY0Mzc2fQ.266jBp-yXRG-_rBXeWHdvw1bgsRYvcghGts1blj2OMw"
headers = {
    "Authorization" : "Bearer {}".format(api_token),
    "content-type" : "application/json",
}

def envoie_event(nom_event, payload):
    payload_str=json.dumps(payload)
    envoie=requests.post(url+nom_event, headers=headers, data=payload_str)
    print(json.loads(envoie.text))

#envoie_event("my_event",{"ma_data": "bonjour monde"})
'''
