# Conversor UTM para KML

Este script Python converte dados de coordenadas no formato UTM (Universal Transverse Mercator) para o formato KML (Keyhole Markup Language), utilizado pelo Google Earth e outros softwares de visualização de mapas.

## Como funciona

O script consiste em três funções principais:

1. `ler_dados(nome_arquivo)`: Esta função lê um arquivo de texto contendo coordenadas UTM e as armazena em uma lista de tuplas no formato (latitude, longitude).
   
2. `converter_utm_para_lat_long(dados)`: Esta função converte as coordenadas UTM para latitude e longitude. Ela utiliza a biblioteca PyProj para realizar essa conversão. Certifique-se de que a zona UTM correta (e se é no hemisfério sul ou não) está configurada dentro desta função.

3. `gerar_kml(nome_arquivo_saida, dados)`: Esta função gera um arquivo KML com os dados convertidos. Os marcadores KML são criados com base nas coordenadas de latitude e longitude.

## Pré-requisitos

Antes de executar o script, é necessário ter Python instalado no seu sistema. Além disso, é preciso instalar a biblioteca PyProj. Você pode instalá-la via pip executando o seguinte comando:

```bash
pip install pyproj
```
## Como rodar

1. Coloque seus dados de coordenadas no formato UTM em um arquivo de texto. Cada linha deve conter uma única coordenada no formato "latitude, longitude".

2. Execute o script `geradorDeAlfinetes.py`,
   
3. O arquivo de entrada deve estar na mesma pasta do script,

Isso irá gerar um arquivo KML chamado `marcadores.kml` com os marcadores correspondentes às coordenadas convertidas.

## Formato dos dados

Certifique-se de que os dados de entrada estejam no formato UTM, com a latitude seguida pela longitude, conforme exemplificado abaixo:

```bash
660000, 680000
```
## Importação 

Após gerar o arquivo KML com o script fornecido, você pode importá-lo no Google Earth para visualizar seus marcadores e outras informações geográficas. Aqui estão as instruções para importar o arquivo KML no Google Earth:

1. Abra o Google Earth: https://earth.google.com/web;
   
2. Clicar em "+ NOVO";
   
3. Clicar em "Arquivo KML local" e escolher o arquivo `marcadores.kml`;

