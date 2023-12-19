from Conexao import Conexao

listaNotas = []

class SemManifesto():
    @staticmethod
    def buscaNFSemManif(path_econfe):
        con = Conexao.conecta(path_econfe)
        if con is False:
            return False
        else:
            select = "select nsu,ciencia from nfe_tbnfesemmanifest tbn"
            aux = con.cursor()
            aux.execute(select)
            empresaSQL = aux.fetchall()

            if empresaSQL is None:
                return False
            else:
                return empresaSQL
