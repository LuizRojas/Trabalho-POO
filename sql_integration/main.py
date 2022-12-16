from cores import Cores
from ubs import UBS
# import os

def operacoes() -> dict:
    escolhas = {
        1: 'Cadastrar UBS',
        2: 'Cadastrar Servidor Municipal',
        3: 'Cadastrar Vacina',
        4: 'Receber Lote de Vacinas',
        5: 'Agendar vacinação',
        6: 'Cancelar agendamento de vacinação',
        7: 'Registrar vacinação efetuada',
        8: '{}Sair do programa{}'.format(Cores.catalogo['azul'], Cores.catalogo['limpa'])}
    return escolhas

def main():
    ops = operacoes()
    print('{}Bem-vindo(a)!{}'.format(Cores.catalogo['verde'], Cores.catalogo['limpa']))

    for key, value in ops.items():  # exibindo as escohas na tela
        print(f'Digite {Cores.catalogo["amarelo"]}{key}{Cores.catalogo["limpa"]} para {value}')

    rodando = True 
    while rodando:

        try:
            entrada = int(input('-> '))
            ubs = UBS()

            if (entrada == 8):
                rodando = False
            
            if entrada == 1:
                nom_ubs = str(input("Digite o nome da UBS: "))
                sgl_ubs = str(input("Digite a sigla da UBS: "))
                
                ubs.cadastrar_ubs(nom_ubs, sgl_ubs)
                ubs.exibir_dados(1)

            if entrada == 2:
                nom_servidor = str(input("Digite o nome do servidor municipal: "))
                mat_servidor = str(input("Digite o numero de matricula: "))
                ubs_servidor = str(input("Digite a sigla da ubs do servidor:  "))
                
                ubs.cadastrar_servidor_municipal(nom_servidor, mat_servidor, ubs_servidor)
                ubs.exibir_dados(2)
                
            if entrada == 3:
                nom_vacina = str(input("Digite o nome da vacina: "))
                fab_vacina = str(input("Digite o nome da fabricante: "))
                doenc_vacina = str(input("Digite o nome da doenca: "))
                
                ubs.cadastrar_vacina(nom_vacina, fab_vacina, doenc_vacina)
                ubs.exibir_dados(3)

            if entrada == 4:
                lot_vac = str(input("Digite a vacina a ser recebida: "))
                unid_bs = str(input("Digite o a sigla da UBS: "))
                qtd_vac = int(input("Digite a quantidade de vacinas recibidas: "))
                # cust_dose = float(round(input("Digite o custo da dose: "), 2))  # arredondando para duas casas decimais
                cust_dose = float(input("Digite o custo da dose: "))
                fonte_lot = str(input("Digite a fonte do lote: "))
                
                ubs.receber_lote_vacina(lot_vac, unid_bs, qtd_vac, cust_dose, fonte_lot)
                ubs.exibir_dados(4)

            if entrada == 5:
                sgl_ubs_agenda = str(input("Digite a sigla da UBS: "))
                vac_agenda = str(input("Digite o nome da vacina a ser tomada: "))
                nom_agenda = str(input("Digite o seu nome: "))
                cpf_agenda = int(input("Digite seu cpf: "))

                ubs.agendar_vacinacao(sgl_ubs_agenda, vac_agenda, nom_agenda, cpf_agenda)
                ubs.exibir_dados(5)
                
            if entrada == 6:
                cpf_cancel = int(input("Digite seu cpf: "))
                ubs.cancelar_agendamento_vacinacao(cpf_cancel)
                ubs.exibir_dados(5)  # exibindo tabela apos cancelamento

            if entrada == 7:
                cpf_efetuado = int(input("Digite seu cpf: "))
                ubs.registrar_vacinacao_efetuada(cpf_efetuado)
                ubs.exibir_dados(6)

            if (entrada > 8) or (entrada < 1):
                print('Número inválido!\nPor favor insira um valor entre {}1 e 8{}!'.format(Cores.catalogo['ciano'], Cores.catalogo['limpa']))

            # os.system("cls")

        except (ValueError or KeyboardInterrupt):
            print('Comando não reconhecido\nPor favor insira um valor inteiro entre {}1 e 8{}!'.format(Cores.catalogo['vermelho'], Cores.catalogo['limpa']))

                    
if __name__ == '__main__':
    main()
