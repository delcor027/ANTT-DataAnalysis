## ETL and Descriptive and Inferential Analysis Challenge

### Import CSV

![image](https://github.com/delcor027/ANTT-DataAnalysis/assets/129231567/4b4642c9-c3eb-48a5-9596-5116da32dc88)

Fiz a importação dos arquivos .csv do site da ANTT utilizando as bibliotecas "os, requests, pandas e html", esse código acessa a URL da página e baixa todos os arquivos com dados, logo após esse código transforma todos os arquivos em apenas 1 .csv, assim facilitando a importação para o SSIS, e ao final do código ele adiciona 3 colunas que logo após serão transformadas em PK.

### Import SSIS

![image](https://github.com/delcor027/ANTT-DataAnalysis/assets/129231567/228f241e-f055-4dc6-a977-7bfc2f92375e)

Logo após fiz a estrutura (projeto) dos dados para os bancos de dados STG e DW, com 1 tabela stage no banco de dados STG e 3 tabelas no banco de dados DW, coloquei as SQL Task para "zerá-las" toda vez que eu executo e também para transformar os ID's em PK e FK para se relacionarem entre elas.
Após executá-lo, as tabelas vão diretamente para meus banco de dados já com os ID's.

### Análises descritivas e Inferenciais

![image](https://github.com/delcor027/ANTT-DataAnalysis/assets/129231567/3699ab31-57e9-4f69-9b61-d3b3c431ae8b)

Esse foi o começo do meu código para começar as análises descritivas e inferenciais, infelizmente quase não tive tempo nesses últimos 10 dias, porém o desafio me levou a muitos, muitos aprendizados mesmo, aprendendo e aplicando no mesmo momento, dedicando as únicas horas disponíveis do meu dia a esse projeto ele foi totalmente rico em conhecimento, saí deste projeto aprendendo o SSIS e o SSMS e utilizando novas bibliotecas de Python. 


