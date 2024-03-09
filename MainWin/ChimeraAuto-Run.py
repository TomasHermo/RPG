import os
import sys
from chimera import runCommand as rc

# Detecta el Numero de Peptidos que se pidio en el RPG ###############
with open("../Parameters/parameters.dat", "r") as bin:
    number_read = int(bin.read())
    print(number_read)

#Traduce todos los aminoacidos de una letra a tres letras
def translate(aminoacid):
    o_to_three = {'C': 'Cys', 'D': 'Asp', 'S': 'Ser', 'Q': 'Gln', 'K': 'Lys',
     'I': 'Ile', 'P': 'Pro', 'T': 'Thr', 'F': 'Phe', 'N': 'Asn',
     'G': 'Gly', 'H': 'His', 'L': 'Leu', 'R': 'Arg', 'W': 'Trp',
     'A': 'Ala', 'V':'Val', 'E': 'Glu', 'Y': 'Tyr', 'M': 'Met'}

    return o_to_three[aminoacid]

#Varaibles
pep = []
pepCount = 0
three = []
aminoCount = 0

#Aqui se abre y lee la lista y el numero de peptidos pedidos
with open ('../peptides.txt') as f:
    for i in range(number_read):
        pep.append(f.readline().rstrip('\n'))

peplength = len(pep[0])

for peptide in pep:
    rc("open "+ "../Parameters/"+str(peplength)+".pdb ")
    for aa in peptide:
        amino = translate(aa)
        aminoCount += 1
        rc("swapaa "+str(amino)+" #0:"+str(aminoCount)+".a")
    pepCount += 1
    rc("write format pdb #0 "+"../Chimera-Peptides/"+str(pepCount)+".pdb")
    aminoCount = 0

    print(pepCount)
