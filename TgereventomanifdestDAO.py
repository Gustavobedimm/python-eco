from Conexao import Conexao

listaNotas = []
con = Conexao.conecta()
class TgereventomanifdestDAO:
    @staticmethod
    def buscaNF(nsu):
        if con is False:
            print("erro na conexao")
            return False
        else:
            select = "select nsu,tipo from tgereventomanifdest tger"
            aux = con.cursor()
            aux.execute(select)
            empresaSQL = aux.fetchall()

            if empresaSQL is None:
                return False
            else:
                return empresaSQL
