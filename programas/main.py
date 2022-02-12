from cores import Cores
from classe_vac import *
from ubs import UBS

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

    for key, value in ops.items():
        print(f'Digite {Cores.catalogo["amarelo"]}{key}{Cores.catalogo["limpa"]} para {value}')

    rodando = True 
    while rodando:

        try:
            entrada = int(input('-> '))
            
            if (entrada == 8):
                rodando = False
            
            if entrada == 1:
                pass
            if entrada == 2:
                UBS.cadastrar_servidor()
                
            if entrada == 3:
                Vacina.cadastrar_vacina()
            
            if entrada == 4:
                pass
            if entrada == 5:
                pass
            if entrada == 6:
                pass
            if entrada == 7:
                pass
            if entrada == 8:
                pass

            if (entrada > 8) or (entrada < 1):
                print('Número inválido!\nPor favor insira um valor entre {}1 e 8{}!'.format(Cores.catalogo['ciano'], Cores.catalogo['limpa']))
        
        except (ValueError or KeyboardInterrupt):
            print('Comando não reconhecido\nPor favor insira um valor inteiro entre {}1 e 8{}!'.format(Cores.catalogo['vermelho'], Cores.catalogo['limpa']))

        finally:
            print('Obrigado pela preferência!')
            rodando = False
                    
if __name__ == '__main__':
    main()
