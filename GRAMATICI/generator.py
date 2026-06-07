from parse import *
import random
from collections import defaultdict
def parse_generator(nume_fisier):
    sections=parse(nume_fisier)
    start=get_section(sections,"start")[0]
    alfabet=get_section(sections,"alfabet")
    reguli=defaultdict(list)
    p=get_section(sections,"reguli")
    for i in p:
        i=i.split("-")
        reguli[i[0]].append(i[1].split())
    return start,alfabet,reguli
def generator(simboluri_curente,reguli):
    rezultat=[]
    for simbol in simboluri_curente:
        if simbol in reguli:
            optiune_aleasa = random.choice(reguli[simbol])
            rezultat.extend(generator(optiune_aleasa, reguli))
        else:
            rezultat.append(simbol)
    return rezultat
start,alfabet,reguli=parse_generator("generator.txt")
n=int(input("Scrie cate 'propozitii' vrei sa generezi:"))
for i in range(n):
    cuvinte_list = generator([start], reguli)
    print(" ".join(cuvinte_list).strip())

            

