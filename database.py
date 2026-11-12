
import pymysql

class ConexaoMySQL:


    def _init_(self):
        self.host = "localhost"
        self.user = "root"
        self.password = ""
        self.database = "endereco"
        self.port = 3306
        self.conexao = None
        self.cursor = pymysql.cursors.DictCursor
    

    def abrir(self):
        try:


            self.conexao = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=slf.database,
                port=self.port,
                cursorclass=pymysql.cursors.DictCursor,
            )


            return self.conexao
        
        except pymysql.MySQLError as erro:

            print(f"Erro ao conectar MySQL: (erro)")
            return None
        

    def fechar(self):
        if self.conexao and self.conexao.open:
            self.conexao.close()
        else:
            print("Nenhuma conexão aberta para fechar.")