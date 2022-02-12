from cores import Cores

class Vacina:
    def __init__(self):
        self._dados = {
            'cadastradas': [],
            'lotes': [],
            'agendamentos': [],
            'cancelamentos': [],
            'efetuadas': []
        }
    
    def cadastrar_vacina(self, nome, fabricante, doenca):
        pass

    def receber_lotes(self, vacina, ubs, quantidade, custoDose, fonte):
        dados = {'vacina': vacina, 'ubs': ubs, 'quantidade': quantidade, 'custoDose': custoDose, 'fonte': fonte}
        if not dados in self._dados['lotes']:
            self._dados['lotes'].append(dados)
        else:
            print('Lote já recebido')

    def agendar_vacinacao(self):
        pass

    def cancelar_agendamento(self):
        pass

    def registrar_vacinacao(self):
        pass

    # @property'
    def exibe_dados(self, chave):
        print(self._dados[chave])


teste = Vacina()
for i in range(2):
    teste.cadastrar_vacina('CoronaVac', 'SinoVac', 'COVID-19')
