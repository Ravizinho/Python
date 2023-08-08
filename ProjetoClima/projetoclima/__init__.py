from request import requisicao

requisicao = requisicao.requisicao(input('Digite o nome da cidade:'))


if requisicao.status_code == 200:
    requisicao_dic = requisicao.json()
else:
    print("Algo deu errado.\r\nStatus code: %s" % requisicao.status_code)
    print("Você pode saber mais sobre o erro em: https://www.google.com.br/search?q=http+status+code+%s" % requisicao.status_code)


descricao = requisicao_dic['weather'][0]['description']
temperatura = requisicao_dic['main']['temp'] - 273.15

print(descricao, f"{temperatura}ºC")