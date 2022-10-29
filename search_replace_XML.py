import csv
import os
import xml.etree.ElementTree as ET
import tkinter
from tkinter import filedialog
import time

# Pour empêcher qu'une fenêtre tkinter non-désirée s'affiche :
tkinter.Tk().withdraw()

print("Script de modification d'un fichier XML à partir d'une liste de chaînes de caractères à rechercher / remplacer "
      "comprise dans un fichier CSV à deux colonnes 'motif de recherche' et 'motif de remplacement'. Les termes
      "utilisés sont sensibles à la casse. Le script créera un nouveau fichier XML avec les modifications demandées.")

time.sleep(5)

# Manifestement, input() empêche filedialog.askopenfilename() de s'exécuter ensuite
# Pas de souci avec print()

# Utilisation de filedialog.askopenfilename()
# Serait filedialog.askdirectory() pour ouvrir un répertoire
input_xml = filedialog.askopenfilename(title="Sélection du fichier XML à modifier")
csv_file = filedialog.askopenfilename(title="sélection du fichier CSV avec les motifs de recherche et de remplacement")
print(f"Le fichier {input_xml} sera modifié dans un nouveau fichier 'output.xml'.\n")
print(f"Les données pour les modifications se trouvent dans le fichier {csv_file}.\n")
input("Appuyez sur Entrée pour continuer.")

# Ouverture du fichier CSV avec les motifs
with open(csv_file, 'r', encoding="utf-8") as liste_csv:
    reader = csv.reader(liste_csv, delimiter = ";")
    # Ouverture du fichier XML
    with open(input_xml, encoding='utf-8') as f:
        tree = ET.parse(f)
        root = tree.getroot()

        # Pour chaque ligne du CSV, on itère sur le motif de recherche et le motif de remplacement
        for row in reader:
            motif_rech = row[0]
            motif_rempl = row[1]
            # à chacune de ces itérations, on boucle également sur le texte du XML. Si on
            # trouve le motif de recherche, il est alors remplacé par son motif de remplacement.
            for element in root.iter():
                try:
                    element.text = element.text.replace(motif_rech, motif_rempl)
                except AttributeError:
                    pass

# Ecriture du fichier de sortie
# Comment ajouter le DOCTYPE avec sa DTD ?
tree.write('output.xml', encoding='utf-8', xml_declaration=True)
print("Les remplacements ont été effectués")
