import datetime
import winsound


def ascii_livro(h: int, m: int):
    if h < 10 > m:
        print('    __________________   __________________')
        print(f'.-/|                  \ /                  |\-.\n||||    O modo         |                   ||||')
        print(f'||||                   |     O programa    ||||\n||||    Atual          |                   ||||')
        print(f'||||                   |     Despertará    ||||\n||||    É Estudo       |                   ||||')
        print(f'||||                   |     Às 0{h}:0{m}      ||||\n||||    ~~~~~~~~       |                   ||||')
        print(f'||||                   |     ~~~~~~~~      ||||\n||||                   |                   ||||')
        print(f'||||                   |                   ||||\n||||__________________ | __________________||||')
        print(f'||/===================\|/===================\||\n`--------------------~___~-------------------''')
    if h < 10 <= m:
        print('    __________________   __________________')
        print(f'.-/|                  \ /                  |\-.\n||||    O modo         |                   ||||')
        print(f'||||                   |     O programa    ||||\n||||    Atual          |                   ||||')
        print(f'||||                   |     Despertará    ||||\n||||    É Estudo       |                   ||||')
        print(f'||||                   |     Às 0{h}:{m}      ||||\n||||    ~~~~~~~~       |                   ||||')
        print(f'||||                   |     ~~~~~~~~      ||||\n||||                   |                   ||||')
        print(f'||||                   |                   ||||\n||||__________________ | __________________||||')
        print(f'||/===================\|/===================\||\n`--------------------~___~-------------------''')
    if h >= 10 > m:
        print('    __________________   __________________')
        print(f'.-/|                  \ /                  |\-.\n||||    O modo         |                   ||||')
        print(f'||||                   |     O programa    ||||\n||||    Atual          |                   ||||')
        print(f'||||                   |     Despertará    ||||\n||||    É Estudo       |                   ||||')
        print(f'||||                   |     Às {h}:0{m}      ||||\n||||    ~~~~~~~~       |                   ||||')
        print(f'||||                   |     ~~~~~~~~      ||||\n||||                   |                   ||||')
        print(f'||||                   |                   ||||\n||||__________________ | __________________||||')
        print(f'||/===================\|/===================\||\n`--------------------~___~-------------------''')
    if h >= 10 <= m:
        print('    __________________   __________________')
        print(f'.-/|                  \ /                  |\-.\n||||    O modo         |                   ||||')
        print(f'||||                   |     O programa    ||||\n||||    Atual          |                   ||||')
        print(f'||||                   |     Despertará    ||||\n||||    É Estudo       |                   ||||')
        print(f'||||                   |     Às {h}:{m}      ||||\n||||    ~~~~~~~~       |                   ||||')
        print(f'||||                   |     ~~~~~~~~      ||||\n||||                   |                   ||||')
        print(f'||||                   |                   ||||\n||||__________________ | __________________||||')
        print(f'||/===================\|/===================\||\n`--------------------~___~-------------------''')


def ascii_xicara(h: int, m: int):
    if h < 10 > m:
        print(f'     (  )   (   )  )\n      ) (   )  (  (\n      ( )  (    ) )\n      _____________')
        print(f'     <_____________> ___\n     |             |/ _ \ \n     |   O modo      | | |')
        print(f'     |   Atual é     |_| |\n  ___|   Descanso  |\___/\n /    \___________/    \.')
        print(f'|  O programa desperará |\n \______Às 0{h}:0{m}_______/')
    if h < 10 <= m:
        print(f'     (  )   (   )  )\n      ) (   )  (  (\n      ( )  (    ) )\n      _____________')
        print(f'     <_____________> ___\n     |             |/ _ \ \n     |   O modo      | | |')
        print(f'     |   Atual é     |_| |\n  ___|   Descanso  |\___/\n /    \___________/    \.')
        print(f'|  O programa desperará |\n \______Às 0{h}:{m}_______/')
    if h >= 10 > m:
        print(f'     (  )   (   )  )\n      ) (   )  (  (\n      ( )  (    ) )\n      _____________')
        print(f'     <_____________> ___\n     |             |/ _ \ \n     |   O modo      | | |')
        print(f'     |   Atual é     |_| |\n  ___|   Descanso  |\___/\n /    \___________/    \.')
        print(f'|  O programa desperará |\n \______Às {h}:0{m}_______/')
    if h >= 10 <= m:
        print(f'     (  )   (   )  )\n      ) (   )  (  (\n      ( )  (    ) )\n      _____________')
        print(f'     <_____________> ___\n     |             |/ _ \ \n     |   O modo      | | |')
        print(f'     |   Atual é     |_| |\n  ___|   Descanso  |\___/\n /    \___________/    \.')
        print(f'|  O programa desperará |\n \______Às {h}:{m}_______/')


def conta_de_horas(estudar: bool, tempo_estudo=1, tempo_descanso=1):
    tempo = datetime.datetime.now()
    if estudar:
        minutos_do_despertar = int(tempo.strftime("%M")) + tempo_estudo
        if minutos_do_despertar > 60:
            minutos_do_despertar = minutos_do_despertar - 60
            horas_do_despertar = int(tempo.strftime("%H")) + 1
            ascii_livro(horas_do_despertar, minutos_do_despertar)
            return horas_do_despertar, minutos_do_despertar

        else:
            ascii_livro(int(tempo.strftime("%H")), minutos_do_despertar)
            return int(tempo.strftime("%H")), minutos_do_despertar

    else:
        minutos_do_despertar = int(tempo.strftime("%M")) + tempo_descanso

        if minutos_do_despertar > 60:
            minutos_do_despertar = minutos_do_despertar - 60
            horas_do_despertar = int(tempo.strftime("%H")) + 1
            ascii_xicara(horas_do_despertar, minutos_do_despertar)
            return horas_do_despertar, minutos_do_despertar

        else:
            ascii_xicara(int(tempo.strftime("%H")), minutos_do_despertar)
            return int(tempo.strftime("%H")), minutos_do_despertar


def musiquinha():
    winsound.Beep(3951, 750)
    winsound.Beep(3136, 750)
    winsound.Beep(3520, 750)
    winsound.Beep(2349, 900)
    winsound.Beep(2349, 750)
    winsound.Beep(3520, 750)
    winsound.Beep(3951, 750)
    winsound.Beep(3136, 900)


def despertar(estudar: bool):
    escolha_ciclos = int(input("Escolha o número de ciclos que você deseja estudar\n"))
    for i in range(escolha_ciclos*2):
        if estudar:
            despertar_horas, despertar_minutos = conta_de_horas(estudar)
            while True:
                tempo = datetime.datetime.now()
                if despertar_horas == int(tempo.strftime('%H')) and despertar_minutos == int(tempo.strftime('%M')):
                    print("\nHora de Relaxar!!!\n")
                    musiquinha()
                    estudar = False
                    break
        else:
            despertar_horas, despertar_minutos = conta_de_horas(estudar)
            while True:
                tempo = datetime.datetime.now()
                if despertar_horas == int(tempo.strftime('%H')) and despertar_minutos == int(tempo.strftime('%M')):
                    print("\nHora de Focar!!!\n")
                    musiquinha()
                    estudar = True
                    break


def tela_principal():
    print('       <#============================================#>')
    print('       |/                Bem-Vindo a                 \|')
    print('       ||              Aplicação de um               ||')
    print('       |\             Relógio de Pomodoro            /|')
    print('       <#============================================#>')
    print("Escolhas:")
    print("1 -> Estudo (padrão 25 minutos)                3 -> Mudar intervalo de tempo")
    escolha = input(f"2 -> Descanso (padrão 5 minutos)               4 -> Infomações\n")
    return escolha


def main():
    while True:
        escolha_do_modo = tela_principal()
        match escolha_do_modo.strip(' '):
            case '1':
                estudar = True
                despertar(estudar)
            case '2':
                estudar = False
                despertar(estudar)
            case '3':
                print('mudar intervalo')
            case '4':
                print('infos')
            case _:
                print("|====\ Digite uma opção válida! /====|")

if __name__ == '__main__':
    main()
