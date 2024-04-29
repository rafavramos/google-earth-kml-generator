from pyproj import Proj

def ler_dados(nome_arquivo):
    dados = []
    with open(nome_arquivo, 'r') as f:
        for line in f:
            latitude, longitude= map(float, line.strip().split(','))
            dados.append((latitude, longitude))
            print(dados)
    return dados

def converter_utm_para_lat_long(dados):
    utm_zone_number = 22  # Defina a zona UTM apropriada para sua localização
    utm_proj = Proj(proj='utm', zone=utm_zone_number, ellps='WGS84', south=True)

    lat_long_dados = []
    for longitude, latitude in dados:
        lat, lon = utm_proj(longitude, latitude, inverse=True)
        print(f'latitude: {lat} longitude {lon}')
        lat_long_dados.append((lat, lon))
    return lat_long_dados

def gerar_kml(nome_arquivo_saida, dados):
    with open(nome_arquivo_saida, 'w') as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<kml xmlns="http://www.opengis.net/kml/2.2">\n')
        f.write('<Document>\n')
        
        for i, (latitude, longitude) in enumerate(dados, start=1):
            f.write('<Placemark>\n')
            f.write(f'<name>Dado {i}</name>\n')
            f.write('<Point>\n')
            f.write(f'<coordinates>{latitude},{longitude}</coordinates>\n')
            f.write('</Point>\n')
            f.write('</Placemark>\n')
        
        f.write('</Document>\n')
        f.write('</kml>\n')

nome_arquivo_entrada = 'dados.txt'
nome_arquivo_saida = 'marcadores.kml'

dados = ler_dados(nome_arquivo_entrada)
dados_lat_long = converter_utm_para_lat_long(dados)
gerar_kml(nome_arquivo_saida, dados_lat_long)
