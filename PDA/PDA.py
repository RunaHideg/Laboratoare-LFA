from parse import parse, get_section

def incarca_pda(nume_fisier):
    sections = parse(nume_fisier)
    alfabet = get_section(sections, "alfabet")
    s = get_section(sections, "stare_initiala")
    stare_initiala = s[0]
    f = get_section(sections, "stari_finale")
    d = get_section(sections, "delta")
    
    delta = []
    for i in d:
        st, dr = i.split("-")
        st_elemente = st.split(",")
        dr_elemente = dr.split(",")  
        delta.append(st_elemente + dr_elemente)
        
    stari = get_section(sections, "stari")
    return alfabet, stari, stare_initiala, f, delta

def validare_pda(cuvant, stare_initiala, stari_finale, delta):
    stare_curenta = stare_initiala
    stiva = ["$"] 
    
    for litera in cuvant:
        if not stiva:
            return False  
        
        varf_stiva = stiva[-1]
        gasit_tranzitie = False
        
        for i in delta:
            if i[0] == stare_curenta and i[1] == litera and i[2] == varf_stiva:
                stare_curenta = i[3] 
                stiva.pop()         
                if i[4] != "eps":
                    for simbol in reversed(i[4]):
                        stiva.append(simbol)
                
                gasit_tranzitie = True
                break  
        
        if not gasit_tranzitie:
            return False  
    stiva_este_curatata = (len(stiva) == 1 and stiva[0] == "$")
    
    return (stare_curenta in stari_finale) and stiva_este_curatata


cuvant = input("Introdu un cuvant pe care sa-l validezi prin PDA: ")
alfabet, stari, s, f, delta = incarca_pda("PDA.txt")

valid_alfa = True
for litera in cuvant:
    if litera not in alfabet:
        print("Nu este valid!")
        valid_alfa = False
        break

if valid_alfa:
    if validare_pda(cuvant, s, f, delta):
        print("Este valid!")
    else:
        print("Nu este valid!")