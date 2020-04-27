import xml.etree.ElementTree as ET
import re

identite = 'identite'
dossier = 'dossier'


def mapEmprunteurIdentite(dossiers, identites):
    exPersonnes = [id[0].text for id in identites]
    print('%d exPersonnes' % len(exPersonnes))
    try:
        for index in range(len(dossiers)-1, 0, -1):
            print('processing dossier %d' % index)
            doss = dossiers[index]
            exPer = ''
            for emprunteur in doss.findall('emprunteur'):
                exPerEmprunteur = emprunteur[0].text
                if(exPerEmprunteur not in exPersonnes):
                    exPer = exPersonnes.pop()
                    print('replacing %s with %s' % (emprunteur[0].text, exPer))
                    emprunteur[0].text = exPer
                else:
                    exPer = emprunteur[0].text

            credit = doss.find('credit')
            credit.set('produit', 'PRDT001')
            for payeur in credit.findall('payeur'):
                payeur[0].text = exPer
    except:
        print('error occurred')


def parseXml():

    with open("data.xml") as f:
        xmlstring = f.read()

    # Remove the default namespace definition (xmlns="http://some/namespace")
    xmlstring = re.sub(r'\sxmlns="[^"]+"', '', xmlstring, count=1)

    tree = ET.ElementTree(ET.fromstring(xmlstring))
    doc = tree.getroot()

    identites = []
    dossiers = []
    for child in doc:
        if (child.tag.endswith(identite)):
            identites.append(child)
        elif (child.tag.endswith(dossier)):
            dossiers.append(child)
    print('Nombre identites : %d' % len(identites))
    print('Nombre Dossiers : %d' % len(dossiers))
    mapEmprunteurIdentite(dossiers, identites)
    tree.write('output.xml')


if __name__ == "__main__":
    parseXml()
