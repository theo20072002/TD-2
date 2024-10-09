import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
np.random.seed(123)

import requests

url = "https://www.insee.fr/fr/statistiques/fichier/6800675/v_commune_2023.csv"
url_backup = "https://minio.lab.sspcloud.fr/lgaliana/data/python-ENSAE/cog_2023.csv"

try:
    response = requests.get(url)
except requests.exceptions.RequestException as e:
    print(f"Error : {e}")
    response = requests.get(url_backup)

# Only download if one of the request succeeded
if response.status_code == 200:
    with open("cog_2023.csv", "wb") as file:
        file.write(response.content)

# afficher la base de donné :
df = pd.read_csv('cog_2023.csv')

print(df)

# importer la base de donné :
url = "https://koumoul.com/s/data-fair/api/v1/datasets/igt-pouvoir-de-rechauffement-global/convert"
emissions=pd.read_csv(url, sep=",")

# donne le repertoir de travail
print(os.getcwd())
#donne les autres fichiers du repertoire
print(os.listdir())

print(emissions[0:10])