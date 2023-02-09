def percorrer_km(litros, consumo_km):
    return consumo_km * litros

litros = int(input('Digite quantos litros de gasolina tem no tanque: '))
consumo_km = 15
print(f'Seu carro irá percorrer: {percorrer_km(litros, consumo_km)}Km')
#A função percorrer_km recebe dois parâmetros: litros e consumo_km. 
#O cálculo para calcular a distância percorrida é feito pela seguinte linha: consumo_km * litros. 
#Este resultado é retornado pela função.


