#gerar exe do projeto
#pip install PyInstaller
#pyinstaller Main.py
from SemManifestoDAO import SemManifesto
from EventosDAO import Eventos
import json
config = json.load(open('./ini.json'))
path_econfe = config['econfe']
opcao = ""
while opcao != "0":
    opcao = input("DIGITE UMA OPÇÃO : \n"
              "1 - VERIFICAR NOTAS DA ABA SEM MANIFESTO\n"
              "0 - SAIR\n")
    if opcao == "1":
        listaNotas = SemManifesto.buscaNFSemManif(path_econfe)
        possuiErro = False
        if listaNotas is False:
            print("erro ao executar a classe SemManifesto.buscaNFSemManif()")
        else:
            for i in listaNotas:
                nsu,ciencia = i
                string_ciencia = str(ciencia)
                string_nsu = str(nsu)
                evento = Eventos.consultaEvento(string_nsu,path_econfe)
                if len(evento) == 0:
                    if string_ciencia == "-1":
                        print("----------------------------------------------------------------------------------------------------------------------------------")
                        print("ERRO : NSU : ",string_nsu, " Ciencia : ", string_ciencia, " - Não foi encontrado o evento de Ciencia da operação na tabela NFE_TBEVENTO para este documento.")
                        print("----------------------------------------------------------------------------------------------------------------------------------")
                        possuiErro = True
                else:
                    if ciencia is None:
                        possuiErro = True
                        print("----------------------------------------------------------------------------------------------------------------------------------")
                        print("ATENÇÃO - Foi encontrado um evento na tabela NFE_TBEVENTO para este documento.")
                        print("NFE_TBNFESEMMANIFEST")
                        if string_ciencia == '-1':
                            print("Nsu:", string_nsu, "Ciencia:", string_ciencia, "***Possui ciencia da operação")
                        else:
                            print("Nsu:", string_nsu, "Ciencia:", string_ciencia,"***Ainda não possui ciencia da operação")
                        for i in evento:
                            nsu,tipoevento,xmotivo,numeroprotocolo,datahoraregistro = i
                            string_tipoevento = str(tipoevento)
                            string_nome_evento = ""
                            if string_tipoevento == "210210":
                                string_nome_evento = "Ciência da Operação"
                            if string_tipoevento == "210200 ":
                                string_nome_evento = "Confirmação da Operação"
                            if string_tipoevento == "210220  ":
                                string_nome_evento = "Desconhecimento da Operação"
                            if string_tipoevento == "210240  ":
                                string_nome_evento = "Operação não Realizada"
                            print("NFE_TBEVENTO")
                            print("NSU : ",nsu,"Tipo Evento : ", tipoevento,"-",string_nome_evento,"- Motivo :",xmotivo,"- Protocolo :",numeroprotocolo,"- Data Registro:",datahoraregistro)
                            if numeroprotocolo is None:
                                print("Provavelmente o evento não foi protocolado")
                        print("----------------------------------------------------------------------------------------------------------------------------------")
        if possuiErro is False:
            print("***Não encontrei nenhum erro! ")
            print(path_econfe)

print("Sistema finalizado.")
exit()
