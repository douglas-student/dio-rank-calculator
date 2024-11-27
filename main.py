import curses

def calculate_balance_and_level(victories, defeats):
    saldo = victories - defeats

    # Determina o nível baseado no número de vitórias
    if victories < 10:
        level = "Ferro"
    elif 10 <= victories <= 20:
        level = "Bronze"
    elif 21 <= victories <= 50:
        level = "Prata"
    elif 51 <= victories <= 80:
        level = "Ouro"
    elif 81 <= victories <= 90:
        level = "Diamante"
    elif 91 <= victories <= 100:
        level = "Lendário"
    else:
        level = "Imortal"
    
    return saldo, level

def get_value(stdscr, label):
    while True:
        stdscr.addstr(label)
        response = stdscr.getstr().decode("utf-8").strip()
        if response.isdigit():
            response = int(response)
            return response
        else:
            stdscr.clear()
            stdscr.addstr("\n Por favor, digite apenas números positivos!\n")
            stdscr.refresh()

def main(stdscr):
    # Inicializa curses
    curses.echo()  # Permite a entrada de texto ser visível
    stdscr.clear()

    # Entrada de vitórias
    victories = get_value(stdscr, "Digite o número de vitórias: ")

    # Entrada de derrotas
    defeats = get_value(stdscr, "Digite o número de derrotas: ")

    # Calcula saldo e nível
    saldo, level = calculate_balance_and_level(victories, defeats)

    # Exibe o resultado no formato correto
    message = f"O Herói tem de saldo de {saldo} e está no nível de {level}"
    stdscr.addstr(f"\n{message}\n")
    stdscr.addstr("Pressione qualquer tecla para sair...")
    stdscr.getch()

# Executa o programa
curses.wrapper(main)
