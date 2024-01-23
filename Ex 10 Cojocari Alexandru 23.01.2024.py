a = input("text:")
cuvinte = a.split()
cuvinte_doua_litere = [cuvant for cuvant in cuvinte if len(cuvant) == 2]
cuvinte_doua_litere.sort()
z = ' '.join(cuvinte_doua_litere)
print("date de iesire:", z)

