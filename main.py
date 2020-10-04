import requests
import json

continuar = True

while continuar == True:

    try:
        print('Moedas disponiveis')
        moedas = requests.get("http://free.currconv.com/api/v7/currencies?apiKey=bffd1f34eb73b1af930e").json()
        for moeda in moedas["results"]:

            print(moeda)

        print("\nDigte a moeda inicial")

        initialCurrency = input()

        print("\nDigte a moeda final ")
        finalCurrency = input()
        json = requests.get("http://free.currconv.com/api/v7/convert?q="+initialCurrency+"_"+finalCurrency+"&compact=ultra&apiKey=bffd1f34eb73b1af930e").json()
        conversao = json[initialCurrency+"_"+finalCurrency]
        print("1 " + initialCurrency + " equivale a " + str(conversao) + " " + finalCurrency)
        conversaoMoedas = open("conversaoMoedas.csv", "w+")
        valorCSV = initialCurrency+"," + str(conversao) + "," + finalCurrency
        conversaoMoedas.writelines(valorCSV)
        conversaoMoedas.close()
        print("\nArquivo Salvo")
    except:
        print('Occrreu um erro')
    finally:
        print("Digite 'S' para digiar outro valor, ou qualquer outra coisa para sair")
        option = input().upper()
        if option == 'S':
            continuar = True
        else:
            continuar = False