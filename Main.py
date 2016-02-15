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

print(moji[0])

print(moji[0].keys())
