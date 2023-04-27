import os
import subprocess
import tkinter as tk
from tkinter import filedialog

# Créer une fenêtre Tkinter pour la sélection des fichiers
root = tk.Tk()
root.withdraw()

# Sélectionner le fichier d'entrée
input_file = filedialog.askopenfilename(title='Sélectionnez le fichier MKV', filetypes=[('Fichiers MKV', '*.mkv')])

# Vérifier si un fichier a été sélectionné
if not input_file:
    print('Aucun fichier sélectionné.')
    exit()

# Demander l'emplacement de sortie
output_dir = filedialog.askdirectory(title='Sélectionnez un dossier de sortie')

# Vérifier si un dossier a été sélectionné
if not output_dir:
    print('Aucun dossier de sortie sélectionné.')
    exit()

# Construire le chemin du fichier de sortie
output_file = os.path.join(output_dir, os.path.splitext(os.path.basename(input_file))[0] + '.mp4')

# Vérifier si le fichier de sortie existe déjà
if os.path.exists(output_file):
    print(f'Le fichier de sortie {output_file} existe déjà.')
    exit()

# Convertir le fichier MKV en MP4 en utilisant ffmpeg
cmd = f'ffmpeg -i "{input_file}" -c:v copy -c:a copy "{output_file}"'
subprocess.call(cmd, shell=True)

# Afficher un message de réussite
print(f'La conversion de {input_file} en {output_file} est terminée.')