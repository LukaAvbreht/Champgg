__author__ = 'Luka'
import Pridobivanje
import json
import re

Pridobivanje.shrani('http://champion.gg/statistics/#?sortBy=general.winPercent&order=descend&roleSort=','champgg.html')

in_file = open("champgg.html")

data = in_file.read()

regex = """<script>\s*matchupData.stats = (?P<podatki>.*);\s*</script>"""

a = re.search(regex, data)

podatki = a.groupdict()["podatki"]

moji = json.loads(podatki)
podatki = list()

for i in moji:
    slovar = dict()
    for j in i:
        if j == 'general':
            for k in i['general']:
                slovar[k] = i['general'][k]
        else:
            slovar[j] = i[j]
    podatki.append(slovar)

def del_el_dict(slovar,element):
    """iz seznama slovarjov pobriše element v vsakem slovarju"""
    for slo in slovar:
        del slo[element]
    return slovar

del_el_dict(podatki,'_id')

Pridobivanje.slovar_csv(podatki,'podatki616.csv',podatki[0].keys())


