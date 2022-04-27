import psycopg2


class Banco:

    def __init__(self, dbname, user, password):
        #definindo privado para respeitar os padrões de OO
        self.__dbname = dbname
        self.__user = user
        self.__password = password

    def __conectar_banco(self):
        try:
            conn = psycopg2.connect('dbname='+self.__dbname+' user=' + self.__user+' password=' + self.__password)       
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        return conn

    def insere_dados_cnpj(self, cnpj, nome, cidade, uf):
        conn = self.__conectar_banco()
        cursor = conn.cursor()
        
        row_count = self.registro_existente(cnpj, nome, cidade, uf)
        #print(row_count)
        if row_count==0:
            try:
                cursor.execute("INSERT INTO filiais (cnpj, nome, cidade, uf) "
                           "VALUES (%s, %s, %s, %s)", (cnpj, nome, cidade, uf))
                conn.commit()
                print('Dados foram inseridos com sucesso!')
            except (Exception, psycopg2.DatabaseError) as error:
                conn.rollback()
                print('Erro na inserção!')
                print(error)
            finally:
                conn.close()
                cursor.close()
        else:
            print('\nEstes registros já estão cadastrados no banco de dados!!')

    def registro_existente(self,cnpj, nome, cidade, uf):
        conn = self.__conectar_banco()
        cursor = conn.cursor()
        ##Validando se os registros existem
        try:
            cursor.execute("SELECT nome FROM filiais WHERE cnpj=%s AND nome=%s AND cidade=%s AND uf=%s ", (cnpj, nome, cidade, uf))
            
            results = cursor.fetchall()
            row_count = cursor.rowcount
            return row_count
        except (Exception, psycopg2.DatabaseError) as error:
            conn.rollback()
            print('Erro na consulta!')
            print(error)
            return -1
        finally:
            conn.close()
            cursor.close()
