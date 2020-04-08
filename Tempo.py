### LINK PRINCIPAL "http://dataservice.accuweather.com/locations/v1/cities/search?apikey=MZGYk1HAS8S7Z1KWRBydMe9P13Tc5db7&q=Araraquara&language=pt-br&alias=SP"
import requests
from pprint import pprint
import json
from datetime import date
def busca(cidade):
    import requests
    import json
    ### GERA NO ACCUWHATEAR ###
    apikey = "shE323HDxvjM0DNYkwnZefDtxGGsrT5o"
    linkbusca = requests.get("http://dataservice.accuweather.com/locations/v1/cities/search?apikey="+apikey+"&q="\
    +cidade+"&language=pt-br")
    conteudo = linkbusca.text
    js = json.loads(conteudo)
    try:
        chave = str(js[0]["Key"])
    except IndexError:
        chave = "Não Existe"
    except KeyError:
        chave = "Não Existe"

    return chave


def previsao():
    apikey = "shE323HDxvjM0DNYkwnZefDtxGGsrT5o"
    cidade = input("Digite o nome da uma cidade: ")
    codigo = busca(cidade)
    if codigo == "Não Existe":
        print("Cidade não encontrada...")
    else:
        requisicao = requests.get("http://dataservice.accuweather.com/forecasts/v1/daily/1day/"+codigo+"?apikey="+apikey+"&language=pt-br&metric=true")
        print(10 *"-#--")
        print(5*"##"+" PREVISÃO DO TEMPO "+5*"##")
        meses = ["JANEIRO","FEVEREIRO","MARÇO","ABRIL","MAIO","JUNHO","JULHO","AGOSTO","SETEMBRO","OUTUBRO","NOVEMBRO","DEZEMBRO"]
        js = json.loads(requisicao.text)
        desc = js["DailyForecasts"][0]["Day"]["IconPhrase"]
        maxima = js["DailyForecasts"][0]["Temperature"]["Maximum"]["Value"]
        minima = js["DailyForecasts"][0]["Temperature"]["Minimum"]["Value"]
        dia = js["DailyForecasts"][0]["EpochDate"]
        mes_formatado = meses[int(date.fromtimestamp(dia).strftime("%m")) + 1]
        ano_formatado = date.fromtimestamp(dia).strftime("%Y")
        dia_formatado = date.fromtimestamp(dia).strftime("%d")
        print("Hoje em %s" %cidade.title()+" dia %s"%dia_formatado+" de %s"%mes_formatado+" de %s"%ano_formatado)
        print(desc)
        print("Temperatura maxima será %sº"%maxima+" com a minima variando a %sº"%minima)
        print(10 *"-#--")
previsao()


