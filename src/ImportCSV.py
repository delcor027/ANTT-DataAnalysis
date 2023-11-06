import os
import requests
import pandas as pd
from lxml import html

repositorio_csv = r'C:\Users\Matheus Delcor\Documents\Programação\AguiaBranca\Base de Dados'

if not os.path.exists(repositorio_csv):
    os.makedirs(repositorio_csv)

url_antt = 'https://dados.antt.gov.br/dataset/acidentes-rodovias'

resposta = requests.get(url_antt)

if resposta.status_code == 200:
    pagina = html.fromstring(resposta.text)

    lista = pagina.xpath('//*[@id="dataset-resources"]/ul/li')

    dataframes = []  # Lista para armazenar os DataFrames

    for indice, lista_de_elemento in enumerate(lista, start=1):
        links_dos_arquivos = lista_de_elemento.xpath('./div/ul/li[2]/a/@href')
        concessionaria = lista_de_elemento.xpath('./a/@title')[0]  # Obtém a concessionária para este arquivo
        concessionaria = concessionaria.replace("Demonstrativos de Acidentes - ", "")

        for arquivos in links_dos_arquivos:
            URL_do_arquivo = arquivos

            nome_do_arquivo = arquivos.split('/')[-1]

            resposta = requests.get(URL_do_arquivo)

            if resposta.status_code == 200:
                if nome_do_arquivo.lower().endswith('.csv') and nome_do_arquivo != 'demostrativo_acidentes_bahia.csv' and nome_do_arquivo != 'demostrativo_acidentes_.csv':
                    with open(os.path.join(repositorio_csv, nome_do_arquivo), 'wb') as arquivo:
                        arquivo.write(resposta.content)

                    print(f'Arquivo {nome_do_arquivo} baixado com sucesso do índice {indice}.')

                    # Lê o CSV e adiciona a coluna "Concessionária"
                    try:
                        df = pd.read_csv(os.path.join(repositorio_csv, nome_do_arquivo), encoding='latin1', delimiter=';', dtype={'coluna2': str}, low_memory=False)
                    except UnicodeDecodeError:
                        df = pd.read_csv(os.path.join(repositorio_csv, nome_do_arquivo), encoding='utf-8', delimiter=';', dtype={'coluna2': str}, low_memory=False)
                        
                    df.insert(0, 'concessionaria', concessionaria)  # Adiciona a coluna "Concessionária" como a primeira
                    dataframes.append(df)  # Adiciona o DataFrame à lista

                    os.remove(os.path.join(repositorio_csv, nome_do_arquivo))
                              
                else:
                    print(f'Arquivo {nome_do_arquivo} não é um arquivo CSV ou não atende às condições.')

            else:
                print(f'Falha ao baixar o arquivo {nome_do_arquivo} do índice {indice}.')

    # Concatena todos os DataFrames na lista em um único DataFrame final
    df_final = pd.concat(dataframes, ignore_index=True)
    
    # Adiciona as colunas listadas abaixo para transformá-las em PK e FK
    df_final.insert(0, 'idAcidentes', df_final.index + 1)
    df_final.insert(1, 'idClassificacao', df_final.index + 1)
    df_final.insert(2, 'idVeiculos', df_final.index + 1)


    # Salva o DataFrame final em um arquivo CSV
    df_final.to_csv(os.path.join(repositorio_csv, 'demostrativo_acidentes.csv'), encoding='latin1', index=False, sep=';')

else:
    print(f'Falha ao acessar a página: {url_antt}')