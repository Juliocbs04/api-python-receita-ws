import requests,psycopg2


class BuscaCnpj:

    def __init__(self, cnpj):
        cnpj = str(cnpj)
        if self.validar_cnpj(cnpj):
            self.cnpj = cnpj
        else:
            raise ValueError("CNPJ inválido")

    def validar_cnpj(self, cnpj):
        if len(cnpj) == 14:
            return True
        else:
            return False
    def formata_cnpj(self):
        return "{}.{}.{}/{}-{}".format(self.cnpj[:2], self.cnpj[2:5], self.cnpj[5:8], self.cnpj[8:12], self.cnpj[12:14])

    def __str__(self):
        return self.formata_cnpj()

    def acessa_via_cnpj(self):
        url = 'https://receitaws.com.br/v1/cnpj/{}'.format(self.cnpj)
        response = requests.get(url)
        dados = response.json()
        if response.status_code == 200:
            print('Requisição retornada com sucesso!')
            #print(response.text)
            string = dados['cnpj']
            dados['cnpj'] = ''.join(char for char in string if char.isalnum())
            return(
                dados['cnpj'],
                dados['nome'],
                dados['municipio'],
                dados['uf']
            )
        else:
            print('Erro na requisição código' + response.status_code)
            return

