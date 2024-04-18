#Apresentação do jogo...
import curses
import time

print("Bem vindo Herói!",end="", flush=True)
time.sleep(2)
print("\rAposto que você tem inúmeras perguntas, mas eu estou aqui para responder a cada uma delas...", flush=True)
time.sleep(3)
#Inicio do jogo, apresentação dos personagens.

def exibir_menu1(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Opção (1): Onde eu estou?")
    stdscr.addstr(1, 0, "Opção (2): O que eu estou fazendo aqui?")
    stdscr.addstr(2, 0, "Opção (3): Quem é você?")
    stdscr.addstr(3, 0, "Opção (4): Não tenho mais perguntas.")
    stdscr.addstr(4, 0, "Opção (5): Sair do jogo.")

def escolher_opcao(stdscr):
    opcao = stdscr.getch()
    return opcao

def main(stdscr):
    curses.curs_set(0)
    while True:
        exibir_menu1(stdscr)
        opcao = escolher_opcao(stdscr)
        if opcao == ord("1"):
         stdscr.addstr(5, 0,"Ah sim, Bom você está em Arcádia um mundo mágico com feras mágicas, monstros, e demônios!")
         stdscr.refresh()
         stdscr.getch()
        elif opcao == ord("2"):
            stdscr.addstr(5, 0,"Não é obvio? Você foi reencarnado como o grande herói que salvará Arcádia das garras do rei demônio!")
            stdscr.refresh()
            stdscr.getch()
        elif opcao == ord("3"):
            stdscr.addstr(5, 0,"Meu nome é Selenia, sou a deusa desse mundo e estou aqui para ajudar a guiar seu caminho e salvar o nosso mundo!")
            stdscr.refresh()
            stdscr.getch()
        elif opcao == ord("4"):
            stdscr.addstr(5, 0,"Tudo bem, nos veremos novamente num futuro próximo...")
            stdscr.refresh()
            stdscr.getch()
            break
        elif opcao == ord("5"):
            stdscr.addstr(5, 0,"Saindo do jogo...")
            stdscr.refresh()
            stdscr.getch()
            break 
        else:
           stdscr.addstr(5, 0,"Opção invalida...")
           stdscr.refresh()

if __name__ == "__main__":
    curses.wrapper(main)