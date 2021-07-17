#Programa que conta as mensagens de uma conversa de whatsapp de cada contacto.
#(suporta apenas os ficheiros.txt atuais da exportação de conversas do whatsapp).
#Versão 3.1.


#Necessário para o sys.exit()
import sys 

# Programa para whatsapp.
import BaseWhatsapp


print("Comandos disponiveis: ajuda, iniciar e sair.")
print("Available commands: help, start and exit.")

#Função que funciona como launcher/hub para tudo.
def hub_start():
    start = input()
    if start == "start" or start == "" or start== "RUN" or start== "Run" or start== "run" or start == "Start" or start == "iniciar" or start == "Iniciar" or start == "começar" or start == "Começar":
        print("A iniciar...")
        print("Starting...")
        print()
        BaseWhatsapp.gotofile()
    elif start == "help" or start == "Help" or start == "HELP" or start == "ajuda" or start == "Ajuda" or start == "AJUDA":
        print('Escreve um comando ("ajuda", "iniciar" ou "sair").')
        print("Atenção á capitalização.")
        print()
        print('Enter a command ("help", "start" or "exit").')
        print("Be aware of the capitalization.")
        hub_start()
    elif start == "exit" or start == "Exit" or start == "EXIT" or start == "sair" or start == "Sair" or start == "SAIR" or start == "Let me out" or start == "LET ME OUT" or start == "Pó caralho!" :
        end()
    else:
        print("Comando não reconhecido.")
        print("Comandos disponiveis: ajuda, iniciar e sair.")
        print()
        print("Invalid command.")
        print("Available commands: help, start and exit.")
        hub_start()
           
def end():
    print("Obrigado por utilizar.")
    print("Thank you for using my program.")
    sys.exit()
 
 
hub_start()