#Programa que conta as mensagens de uma conversa de whatsapp de cada contacto.
#(suporta apenas os ficheiros.txt atuais da exportação de conversas do whatsapp).
#Versão 3.1.


#Necessário para o sys.exit()
import sys 
#Necessário para o time.sleep()
#import time
#Necessário para o os.path.isfile()
import os.path
import main


#Pede o nome do ficheiro e caso não exista, avisa o utilizador. 
def getfile():
    print('Cola o nome do fixeiro aqui (Inclui o ".txt").')
    print("Deixa em branco para usar o ficheiro default." 'Escreve "sair" para sair.')
    print()
    print("Paste the file name here (don't forget the" + ' ".txt" extention).')
    print("Leave it blanck to use the default file." 'Write "quit" to exit.' )
    file = input()
    if file == "quit" or file == "sair":
        main.hub_start();
    if file == "":
        file = "Teste.txt"
    if file[-4:] != ".txt":
        file += ".txt"
    if os.path.isfile(file) == False:
        print("Ficheiro não encontrado.")
        print("File not found.")
        print()
        getfile()
    analize(file)

def analize(file):
    filevar = file
    Speakers = []
    SpeakerNumbers = []
    SpeakerCharacters = []
    SpeakerSpaces = []
    AnomalyCount = 0
    mensagens = 0

    
    
    myfile = open(filevar, "r" , encoding="UTF-8")
    while myfile:
        line  = myfile.readline()
        Anomalia = False
        if line[2:3] == "/" and line[5:6] == "/" and line[8:9] == "," and line[12:13] == ":" and line[16:17] == "-":
            mensagens += 1
            i = 18
            while line[i:i+2] != ": " :
                
                if line[i:i+1] == "":
                    print("Anomalia.")
                    print("Anomaly.")
                    print(line)
                    print()
                    Anomalia = True
                    break
                i += 1
                
            if Anomalia == False:
                Speaker = line[18:i]
                i = 18
                spaces = 0
                letras = 0
                while line[i:i+1] != "":
                    if line [i] == " ":
                        spaces += 1
                    else:
                        letras += 1
                    i +=1
                if not Speaker in Speakers:
                    Speakers.append(Speaker)
                    SpeakerNumbers.append(0)
                    SpeakerCharacters.append(0)
                    SpeakerSpaces.append(0)
                n = Speakers.index(Speaker)
                SpeakerNumbers[n] += 1
                SpeakerCharacters[n] += letras
                SpeakerSpaces[n] += spaces
                
            elif Anomalia == True:
                AnomalyCount += 1
                Anomalia = False
            else:
                print("Erro determinação da identidade.")
                print("Failed to identify the speaker.")
                sys.exit()

        if line == "":
            break
    myfile.close()


    print(str(mensagens-AnomalyCount) + " Mensagens.")
    print(str(AnomalyCount) + "Anomalias.")
    print()
    print(str(mensagens-AnomalyCount) + " Mensages.")
    print(str(AnomalyCount) + "Anomalies.")

    ##apenas usado para testes (troubleshooting)
    #print (Speakers)
    #print (SpeakerNumbers)
    #print (SpeakerSpaces)
    #print (SpeakerCharacters)

    outputExperimental(Speakers,SpeakerNumbers,SpeakerSpaces,SpeakerCharacters)
    # output(Speakers,SpeakerNumbers,SpeakerSpaces,SpeakerCharacters)

    

def output(Speakers,SpeakerNumbers,SpeakerSpaces,SpeakerCharacters):
    print()
    print("Who: - Messages: - Spaces: - Characters: - Words: - Words per message: - words per character")
    print("\n")
    lenght = len(Speakers)
    y = 0
    while y < lenght:
        print(str(Speakers[y]) + "  Messages:" + str(SpeakerNumbers[y]) + "  Spaces:" + str(SpeakerSpaces[y]) + "  Characters:" + str(SpeakerCharacters[y]) + "  Words:" + str(SpeakerSpaces[y] + 1) + "  Words per message:" + str((SpeakerSpaces[y] + 1)/SpeakerNumbers[y]) + "  characters per word:" + str((SpeakerCharacters[y])/(SpeakerSpaces[y] + 1)))
        y += 1
        print()
    main.hub_start()    

def howLong(string,max):
    return max-len(str(string))



def outputExperimental(Speakers,SpeakerNumbers,SpeakerSpaces,SpeakerCharacters):
# from : "https://careerkarma.com/blog/python-typeerror-list-indices-must-be-integers-or-slices-not-str/"
# for s in range(len(students)):
# 	if students[s]["name"] == to_find:
# 		print("The age of {} is {}.".format(students[s]["name"], students[s]["age"]))
    columns =(Speakers,SpeakerNumbers,SpeakerSpaces,SpeakerCharacters)

    print()
    # # intervinients = len(Speakers)
    # longSpeeker = len(Speakers[1])
    # for i in Speakers:
    #     if longSpeeker < len(Speakers[i]):
    #         longSpeeker = len(Speakers[i])
    # for i in Speakers:
    #     print(Speakers[i] + ' '* howLong(Speakers[i],longSpeeker) + '|')



    # longSpeeker = len(Speakers[1])
    # for i in range(len(Speakers)):
    #     if longSpeeker < len(Speakers[i]):
    #         longSpeeker = len(Speakers[i])

    
    # for i in range(len(Speakers)):
    #     print('-'* longSpeeker + '|')
    #     #print(' '* longSpeeker + '|')
    #     print(Speakers[i] + ' '* howLong(Speakers[i],longSpeeker) + '|')
    #     print(' '* longSpeeker + '|')
    #     print(' '* longSpeeker + '|')
    #     #print('-'* longSpeeker + '|')
    

    # for j in range(len(columns)):
    #     longElement = len(str(columns[j][0]))
    #     for i in range(len(columns[j])):
    #         if longElement < len(str(columns[j][i])):
    #             longElement = len(str(columns[j][i]))

        
    #     for i in range(len(columns[j])):
    #         print('-'* longElement + '|')
    #         #print(' '* longElement + '|')
    #         print(str(columns[j][i]) + ' '* howLong(columns[j][i],longElement) + '|')
    #         print(' '* longElement + '|')
    #         print(' '* longElement + '|')
    #         #print('-'* longElement + '|')
    longElement=[]
    for j in range(len(columns)):
        longElement.append(100)
        longElement[j] = len(str(columns[j][0]))
        for i in range(len(columns[j])):
            if longElement[j] < len(str(columns[j][i])):
                longElement[j] = len(str(columns[j][i]))
    
    
    # print(longElement)#temp

        
    # for j in range(len(columns)):
    #     for i in range(len(columns[j])):
    #         print('-'* longElement[j] + '|')
    #         #print(' '* longElement + '|')
    #         print(str(columns[j][i]) + ' '* howLong(columns[j][i],longElement[j]) + '|')
    #         print(' '* longElement[j] + '|')
    #         print(' '* longElement[j] + '|')
    #         #print('-'* longElement + '|')

    for j in range(len(columns[0])):#LINE
        # for k in range(4):
        for i in range(len(columns)):#COLUMN
            print('|' + '-'* longElement[i],end="")
        print("|")
        for i in range(len(columns)):#COLUMN
            print('|' + str(columns[i][j]) + ' '* howLong(columns[i][j],longElement[i]),end="")
        print("|")
        for i in range(len(columns)):#COLUMN
            print('|' + ' '* longElement[i],end="")
        print("|")
        for i in range(len(columns)):#COLUMN
            print('|' + ' '* longElement[i],end="")
        print("|")
    for i in range(len(columns)):#COLUMN
            print('|' + '-'* longElement[i],end="")
    print("|")