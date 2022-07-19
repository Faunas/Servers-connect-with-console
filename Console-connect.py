import webbrowser
from time import sleep

import art
import colorama
from colorama import Fore, Back, Style
colorama.init()
ART1 = art.text2art('CHIPOLINO FUN', '6x10')
a = 0
ART = '''
  ,ad8888ba,   88        88  88  88888888ba     ,ad8888ba,    88           88  888b      88    ,ad8888ba,        88888888888  88        88  888b      88  
 d8"'    `"8b  88        88  88  88      "8b   d8"'    `"8b   88           88  8888b     88   d8"'    `"8b       88           88        88  8888b     88  
d8'            88        88  88  88      ,8P  d8'        `8b  88           88  88 `8b    88  d8'        `8b      88           88        88  88 `8b    88  
88             88aaaaaaaa88  88  88aaaaaa8P'  88          88  88           88  88  `8b   88  88          88      88aaaaa      88        88  88  `8b   88  
88             88""""""""88  88  88""""""'    88          88  88           88  88   `8b  88  88          88      88"""""      88        88  88   `8b  88  
Y8,            88        88  88  88           Y8,        ,8P  88           88  88    `8b 88  Y8,        ,8P      88           88        88  88    `8b 88  
 Y8a.    .a8P  88        88  88  88            Y8a.    .a8P   88           88  88     `8888   Y8a.    .a8P       88           Y8a.    .a8P  88     `8888  
  `"Y8888Y"'   88        88  88  88             `"Y8888Y"'    88888888888  88  88      `888    `"Y8888Y"'        88            `"Y8888Y"'   88      `888 
  '''


ART = '''###   #   #   ###   ####    ###   #       ###   #   #   ###          #####  #   #  #   #
 #   #  #   #    #    #   #  #   #  #        #    #   #  #   #         #      #   #  #   #
 #      #   #    #    #   #  #   #  #        #    ##  #  #   #         #      #   #  ##  #
 #      #####    #    ####   #   #  #        #    # # #  #   #         ####   #   #  # # #
 #      #   #    #    #      #   #  #        #    #  ##  #   #         #      #   #  #  ##
 #   #  #   #    #    #      #   #  #        #    #   #  #   #         #      #   #  #   #
  ###   #   #   ###   #       ###   #####   ###   #   #   ###          #       ###   #   # '''
print(ART1)
print('')
print(Fore.MAGENTA+'---На какой сервер хочешь присоединиться?---\n'+Fore.RED)
print(Fore.RED+'Напиши цифру "1" если хочешь присоединиться на ' +Fore.BLUE +'AWP PROJECT [NO DEAGLE]'+Style.RESET_ALL)
sleep(0.5)
print(Fore.RED+'Напиши цифру "2" если хочешь присоединиться на '+Fore.BLUE +'AWP PROJECT [MIX MAPS]'+Style.RESET_ALL)
sleep(0.5)
print(Fore.RED+'Напиши цифру "3" если хочешь присоединиться на '+Fore.BLUE +'RICHLAND [ONLY MIRAGE]'+Style.RESET_ALL)
sleep(0.5)
print(Fore.RED+'Напиши цифру "4" если хочешь присоединиться на '+Fore.BLUE +'RICHLAND [MIRAGE + DUST2]'+Style.RESET_ALL)
sleep(0.5)
colorama.init()
print(Fore.CYAN+'Чтобы открыть наш сайт - напиши цифру "9"'+Style.RESET_ALL)
while a != 1:
    choose = (input(Style.RESET_ALL+'Напиши выбранную тобой цифру: '))
    try:
        if choose == '1':
            webbrowser.open('steam://connect/212.20.41.198:27084')  # AWP PROJECT [NO DEAGLE]
            a = 1
        elif choose == '2':
            webbrowser.open('steam://connect/212.164.235.137:27058')  # AWP PROJECT [MIX MAPS]
            a = 1
        elif choose == '3':
            webbrowser.open('steam://connect/46.50.165.22:27105')  # RICHLAND [ONLY MIRAGE]
            a = 1
        elif choose == '4':
            webbrowser.open('steam://connect/212.164.235.137:27052')  # RICHLAND [MIRAGE + DUST2]
            a = 1
        elif choose == '9':
            webbrowser.open('https://chipolino.fun/')  # RICHLAND [MIRAGE + DUST2]
            print(Fore.MAGENTA+'Сайт открыт, может теперь зайдём на сервер?')
        else:
            print(Fore.RED+'Нужно вводить только цифры из списка'+Style.RESET_ALL)
    except:
        print(Fore.RED+'Нужно вводить только цифры из списка'+Style.RESET_ALL)
