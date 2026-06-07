from parse import *

def incarca_dfa(nume_fisier):
    sections=parse(nume_fisier)
    alfabet=get_section(sections,"alfabet")
    s=get_section(sections,"stare_initiala")
    stare_initiala=s[0]
    f=get_section(sections,"stari_finale")
    d=get_section(sections,"delta")
    delta=[]
    for i in d:
        delta.append(i.split('-'))
    stari=get_section(sections,"stari")

    return alfabet, stari, stare_initiala,f,delta
def validare(cuvant,stare_initiala,stare_finala,delta):
    stare_curenta=stare_initiala
    for litera in cuvant:
        gasit=False
        for i in delta:
            if stare_curenta==i[0] and litera==i[1]:
                stare_curenta=i[2]
                gasit=True
                break
        if gasit==False:
            return False
    if stare_curenta in stare_finala:
        return True
    else:
        return False
cuvant=input("Introdu un cuvant pe care sa-l validezi:")
alfabet,stari,s,f,delta=incarca_dfa("DFA.txt")
valid_alfa=True
for litera in cuvant:
    if litera not in alfabet:
        print("Nu este valid!")
        valid_alfa = False
        break
if valid_alfa:
    if validare(cuvant, s, f, delta):
        print("Este valid!")
    else:
        print("Nu este valid!")