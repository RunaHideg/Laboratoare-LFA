def parse(nume_fisier):
    sections={}
    s=""
    with open(nume_fisier) as f:
        for linie in f:
            linie=linie.strip()
            if linie[:2]!="//" and linie!="":
                if linie[-1]==":":
                    s=linie[:-1]
                    sections[s]=[]
                else:
                    if s in sections:
                        sections[s].append(linie)
    return sections
def get_section(sections,section_name):
    return sections[section_name]


