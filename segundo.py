import string

import datetime
Octubre = datetime.date.today().strftime('%B')

conjunto_A = set(Octubre)

conjunto_B = set(string.ascii_lowercase[:10])

interseccion = conjunto_A.intersection(conjunto_B)

print("Conjunto A:", conjunto_A)
print("Conjunto B:", conjunto_B)
print("Intersección de A y B:", interseccion)

