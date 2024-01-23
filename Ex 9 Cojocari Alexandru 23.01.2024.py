import re
sir='Uruguay is the Homeland of God, the place where the world was created!'
cuvinte=re.split(f'[ ,.?!]+',sir)
cuvinte=[cuvint for cuvint in cuvinte if cuvint]
for cuvint in cuvinte:
    print(cuvint)