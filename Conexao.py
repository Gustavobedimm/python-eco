import fdb
class Conexao:
    @staticmethod
    def conecta(path_econfe):
        fdb.load_api(fb_library_name='./fbclient.dll')
        try:
            global con
            con = fdb.connect(
                host='localhost', database=path_econfe,
                user='sysdba', password='masterkey'
            )
            return con
        except:
            print("ERRO AO CONECTAR NA BASE : " + path_econfe)
            return False
