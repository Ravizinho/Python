import requests
class requisicao:
    def __init__(self) -> None:
        pass


    def requisicao(nomeDaCidade):
        API_KEY = "89a1b6c243e59104a3069e74fd9d82d1"
        ##lat=-8.0539
        ##lon=-34.8811
        link = f"https://api.openweathermap.org/data/2.5/weather?q={nomeDaCidade}&appid={API_KEY}&lang=pt_br"
        ##link = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={API_KEY}"
        try:    
            requisicao = requests.get(link)
        except:
            requisicao = 'Não foi possível realizar a requisição!'
        return requisicao