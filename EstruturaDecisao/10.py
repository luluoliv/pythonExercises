turno = input("""Em que turno você estuda?
            M - MATUTINO
            V - VESPERTINO
            N - NOTURNO
                            """)

match turno:
    case "M":
        print("Bom dia!")
    case "V":
        print("Boa tarde!")
    case "N":
        print("Boa noite!")
    case _:
        print("Inválido.")

