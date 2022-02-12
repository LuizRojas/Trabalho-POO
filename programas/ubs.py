class UBS:
    def __init__(self):
        self._dados = {
            'ubs cadastradas': [],
            'servidores cadastrados': []
        }
    
    def cadastrar_ubs(self, nome, sigla):
        dados = {'nome': nome, 'sigla': sigla}
        if not dados in self._dados['ubs cadastradas']:
            self._dados['ubs cadastradas'].append(dados)

    def cadastrar_servidor(self, nome, matricula, ubs):
        dados = {'nome': nome, 'matricula': matricula, 'ubs': ubs}
        if not dados in self._dados['servidores cadastrados']:    
            self._dados['servidores cadastrados'].append(dados)


# t1 = UBS()
# t1.exibe_dados('ubs cadastradas')