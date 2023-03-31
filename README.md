# Projeto integrador de computação 3

Neste repositorio estão os arquivos elaborados e utilizados pela equipe para a confecção do projeto de desenvolvimento dos Processos de Ciência de Dados proposto em sala utilizando como escopo a pergunta "Como condições climaticas e geograficas afetam a escolha de métodos de geração de energia"

## Elucidando o projeto

Nesse projeto foi elaborado um processo de ETL. Nosso grupo utilizou duas fontes de dados, uma do Instituto Nacional de Meteorologia (INMET), que contém dados climáticos sobre o território brasileiro, e outra da Agência Nacional de Energia Elétrica (ANEEL), que contém informações sobre empreendimentos de geração de energia no Brasil.
As bases de dados foram extraídas manualmente dos seus respectivos sites.

### Para os dados climáticos foi acessada a base de dados da Agência Nacional de Energia Elétrica, o grupo seguiu o seguinte processo:

#### Acessar o site do INMET pelo link: https://portal.inmet.gov.br/dadoshistoricos

#### Ir até a aba de "Dados metereológicos"

#### Selecionar "Histórico de dados metereológicos"

#### Selecionar os dados do ano de 2022

#### Após isso um download de um arquivo rar vai se iniciar, basta extraí-lo para urilizar a base de dados.

### Para os dados de empreendimento foi acessada a base de dados do Instituto Nacional de Meteorologia, o grupo seguiu o seguinte processo:

#### Acessar o site dos dados abertos da Agência Nacional de Energia Elétrica pelo link: https://dadosabertos.aneel.gov.br

Para cada uma dessas fontes de dados, a equipe utilizou o Jupyter Notebook e a biblioteca Pandas para fazer a leitura dos dados, realizar a transformação necessária e, em seguida, salvar os dados em arquivos no formato CSV.

No caso dos dados de empreendimentos de geração de energia, a equipe selecionou apenas as colunas relevantes para a análise que estavam presentes no arquivo original e salvou os dados filtrados em um novo arquivo CSV.

Já no caso dos dados meteorológicos, a equipe fez o processamento em duas etapas. Primeiro, foi necessário ler vários arquivos CSV que continham informações meteorológicas de diferentes estações de medição do INMET. Em seguida, a equipe selecionou apenas as colunas relevantes e salvou os dados em um novo arquivo CSV.

Todo esse processo é importante para garantir que os dados estejam limpos, organizados e em um formato adequado para análise posterior.



