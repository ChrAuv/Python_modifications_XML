import csv
import os
import xml.etree.ElementTree as ET

input_xml = input("entrer le chemin complet et le nom du fichier XML à modifier.\n")
csv_file = input("entrer le chemin complet et le nom du fichier CSV.\n")

with open(csv_file, 'r', encoding="utf-8") as liste_csv:
    reader = csv.reader(liste_csv, delimiter = ";")
    with open(input_xml, encoding='utf-8') as f:
        tree = ET.parse(f)
        root = tree.getroot()
        print(root)

        i = 0
        for row in reader:
            motif_rech = row[0]
            motif_rempl = row[1]
            for element in root.iter():
                try:
                    element.text = element.text.replace(motif_rech, motif_rempl)
                except AttributeError:
                    pass

tree.write('output.xml', encoding='utf-8')
print(f"{i} remplacements effectués")
