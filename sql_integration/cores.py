import colorama
from colorama import Fore, Style

colorama.init()

class Cores:
    catalogo = {
        'azul': Fore.BLUE,
        'vermelho': Fore.RED,
        'ciano': Fore.CYAN,
        'verde': Fore.GREEN,
        'amarelo': Fore.YELLOW,
        'branco' : Fore.WHITE,
        'magenta': Fore.MAGENTA,
        'azul claro': Fore.LIGHTBLUE_EX,
        'limpa': Style.RESET_ALL
    }
