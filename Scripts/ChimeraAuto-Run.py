# -*- coding: utf-8 -*-
import os
import sys
from chimera import runCommand as rc





# Detecta el Numero de Peptidos que se pidio en el RPG ###############
with open("../Parameters/parameters.dat", "r") as bin:
    # Lee la primera línea y guárdala en una variable
    start = bin.readline().strip()

    # Lee la segunda línea y guárdala en otra variable
    end = bin.readline().strip()

    bin.flush()
    bin.close()


# Imprime las variables para verificar
print("Línea 1:", start)
print("Línea 2:", end)

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
start = int(start)+1
end = int(end)

try:
#Aqui se abre y lee la lista y el numero de peptidos pedidos
    with open ('../random.txt', 'r') as f:
        for i, line in enumerate(f, 1):
            if i >= start and i <= end:
                clean_line = line.rstrip('\n')
                #print(clean_line)
                pep.append(clean_line)

            if i > end:
                break

        # for i in range((num_op*0),(num_op*1)):
        #     pep.append(f.readline().rstrip('\n'))

    peplength = len(pep[0])

    for peptide in pep:
        rc("open "+ "../Parameters/"+str(peplength)+".pdb ")
        for aa in peptide:
            amino = translate(aa)
            aminoCount += 1
            rc("swapaa "+str(amino)+" #0:"+str(aminoCount)+".a")
        pepCount += 1
        name = pepCount + start - 1
        print(str(start) + "Start")
        print(str(name) + "Name")
        rc("write format pdb #0 "+"../Chimera-Peptides/"+str(name)+".pdb")
        aminoCount = 0

except Exception as e:
    print("Error al ejecutar el comando:", e)