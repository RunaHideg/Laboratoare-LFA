from parse import parse, get_section

def epsilon(stari_initiale, delta):
    closure = set(stari_initiale)
    stack = list(stari_initiale)
    
    while stack:
        stare = stack.pop()
        for i in delta:
            if stare == i[0] and i[1] == "eps":
                if i[2] not in closure:
                    closure.add(i[2])
                    stack.append(i[2])
    return closure

def incarca_nfa(nume_fisier):
    sections = parse(nume_fisier)
    alfabet = get_section(sections, "alfabet")
    s = get_section(sections, "stare_initiala")
    stare_initiala = s[0]
    f = get_section(sections, "stari_finale")
    d = get_section(sections, "delta")
    
    delta = []
    for i in d:
        delta.append(i.split('-'))
    stari = get_section(sections, "stari")

    return alfabet, stari, stare_initiala, f, delta

def validare_nfa(cuvant, stare_initiala, stari_finale, delta):
    stari_curente = epsilon({stare_initiala}, delta)
    
    for litera in cuvant:
        urmatoarele_stari = set()
        
        for s in stari_curente:
            for i in delta:
                if s == i[0] and litera == i[1]:
                    urmatoarele_stari.add(i[2])
        
        stari_curente = epsilon(urmatoarele_stari, delta)
        
        if not stari_curente:
            return False

    for s in stari_curente:
        if s in stari_finale:
            return True
    return False

cuvant = input("Introdu cuvântul pentru NFA: ")
alfabet, stari, s, f, delta = incarca_nfa("NFA.txt")

valid_alfa = True
for litera in cuvant:
    if litera not in alfabet:
        print("Nu este valid!")
        valid_alfa = False
        break

if valid_alfa:
    if validare_nfa(cuvant, s, f, delta):
        print("Cuvantul este valid!")
    else:
        print("Cuvantul nu este valid!")