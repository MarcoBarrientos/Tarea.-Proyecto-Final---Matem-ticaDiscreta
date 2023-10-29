total_pares = 0

for primer_digito in range(2, 8):
    for segundo_digito in range(10):
        for tercer_digito in range(10):
            for cuarto_digito in range(10):
                for quinto_digito in range(10):
                    for sexto_digito in range(10):
                        for septimo_digito in range(10):
                            for octavo_digito in range(0, 10, 2):
                                total_pares += 1

print("Número total de números telefónicos pares en Guatemala:", total_pares)

