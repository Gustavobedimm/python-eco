import fdb
class Conexao:
    @staticmethod
    def conecta():
        fdb.load_api(fb_library_name='C:/Program Files/Firebird/Firebird_2_5/bin/fbclient.dll')
        try:
            global con
            con = fdb.connect(
                host='localhost', database='C:/ecosis/dados/ecodados.eco',
                user='sysdba', password='masterkey'
            )
            print("conectado com sucesso")
            return con
        except:
            print("erro de conexao")
            return False
