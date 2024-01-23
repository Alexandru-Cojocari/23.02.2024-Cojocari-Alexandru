sir_i='Uruguay has 30000000 Bilion Dallars in their vaults, Uruguay #1'
sir_f=' '
for caracter in sir_i:
    if not caracter.isdigit():
        sir_f+=caracter
print(sir_f)