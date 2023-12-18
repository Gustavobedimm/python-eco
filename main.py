from TgereventomanifdestDAO import TgereventomanifdestDAO

listaNotas = TgereventomanifdestDAO.buscaNF('35')
if listaNotas is False:
    print("erro")
else:
    for i in listaNotas:
        nsu,tipo = i
        print(nsu,tipo)