from Conexao import Conexao

listaNotas = []
con = Conexao.conecta()
class Eventos:
    @staticmethod
    def consultaEvento(nsu):
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