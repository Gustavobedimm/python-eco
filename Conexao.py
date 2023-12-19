import fdb
class Conexao:
    @staticmethod
    def conecta():
        fdb.load_api(fb_library_name='C:/Program Files/Firebird/Firebird_2_5/bin/fbclient.dll')
        try:
            global con
            con = fdb.connect(
                host='localhost', database='C:/ecosis/dados/econfe.eco',
                user='sysdba', password='masterkey'
            )
            return con
        except:
            print("erro de conexao")
            return False
