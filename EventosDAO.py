from Conexao import Conexao

listaNotas = []

class Eventos:
    @staticmethod
    def consultaEvento(nsu,path_econfe):
        con = Conexao.conecta(path_econfe)
        if con is False:
            return False
        else:
            select = 'select tbn.nsu, evento.tipoevento from NFE_TBNFECONSNFEDESTNFE tbn inner join nfe_tbevento evento on evento.chavenfe = tbn.chavenfe where tbn.nsu = ' + nsu
            #print(select)
            aux = con.cursor()
            aux.execute(select)
            empresaSQL = aux.fetchall()

            if empresaSQL is None:
                return False
            else:
                return empresaSQL