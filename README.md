# Projeto integrador de computação 3

Neste repositorio estão os arquivos elaborados e utilizados pela equipe para a confecção do projeto de desenvolvimento dos Processos de Ciência de Dados proposto em sala utilizando como escopo a pergunta "Como condições climaticas e geograficas afetam a escolha de métodos de geração de energia".

# Porque foi selecionado o modelo de Regressão Logistica?

A utilização de um modelo de aprendizagem de máquina para analisar como os fatores climáticos afetam a geração de energia em cada região do Brasil é um fator determinante para esta escolha, que é a complexidade dos dados. Os fatores climáticos podem ser complexos e variáveis, envolvendo múltiplas variáveis ​​e padrões não lineares. Os modelos de aprendizagem de máquina são capazes de capturar essas complexidades e relacionamentos não triviais entre os dados climáticos e a geração de energia, porém, o primeiro que foi testado foi a Regressão Linear, porém, como mencionado antes, este modelo envolve múltiplas variáveis e padrões não lineares, portanto não foi adequado para este problema, em seguida testamos a hipótese com o modelo de Regressão Logistica que trabalha melhor com padrões não lineares. Depois de testar "Regressão Logistica" tivemos problemas em testar este modelo pois para que o teste funcione ele precisava de 32Gb de memória RAM do computador que foi utilizado, como não somos herdeiros, não temos tal poder computacional. Em seguida, tentamos utilizar a arvore de decisão



Terceira Entrega:
Turma de Terças: 20/06/2023 | Turma de Sextas: 23/06/2023
- Essa entrega será composta de:
  - Desenvolvimento de um Modelo de Aprendizagem de Máquina
  1. Seleção do Modelo
    - Discussão sobre os diferentes tipos de modelos de aprendizagem de
  máquina que poderiam ser aplicados ao conjunto de dados.
    - Justificativa da escolha do modelo selecionado, levando em
  consideração a pergunta de dados e a natureza dos dados disponíveis.
  2. Balanceamento dos Dados
    - Verificação e tratamento de possíveis desequilíbrios nos dados, caso
  seja necessário, por meio de técnicas como oversampling ou
  undersampling.
  3. Treinamento do Modelo
    - Implementação do modelo selecionado em um ambiente de
  desenvolvimento de aprendizagem de máquina (por exemplo, Python
  com bibliotecas como Scikit-learn, Tensorflow ou PyTorch).
    - Treinamento do modelo usando técnicas apropriadas, como validação
  cruzada, para garantir que ele seja capaz de generalizar
  adequadamente para novos dados.
  4. Avaliação do Modelo
    - Avaliação do modelo treinado, incluindo métricas de desempenho
  relevantes, como precisão, recall, F1-score, curva ROC, MAE, MSE,
  RMSE, Silhouete Score.
  5. Aplicação do Modelo
    - Aplicação do modelo em novos dados e interpretação dos resultados
  obtidos.
    - Discussão sobre as possíveis implicações práticas da aplicação do
  modelo em um cenário real.
  6. Conclusão
    - Nesta seção, vocês deverão resumir as principais descobertas e
  conclusões do projeto, incluindo as perguntas levantadas na primeira
  etapa, os resultados da análise exploratória, as conclusões da
  aplicação do modelo de aprendizagem de máquina e as limitações do
  trabalho. Além disso, deverão apresentar sugestões de trabalhos
  futuros que possam expandir ou aprimorar o projeto.
  7. Apresentação Final do Projeto
    - Criação de um relatório final ou Jupyter Notebook que descreve todo
  o processo de engenharia de dados, análise de dados e
  desenvolvimento de modelo de aprendizagem de máquina.
    - Inclusão de gráficos, tabelas e visualizações relevantes que suportam
  os resultados obtidos.
    - Apresentação do projeto em um vídeo, disponibilizado no Youtube,
  que explique de forma clara e coerente todo o processo e resultados
  alcançados, incluindo a criatividade aplicada no desenvolvimento do
  modelo.
    - Disponibilização de todos os scripts utilizados/criados no Github do grupo.
- Criatividade: vocês poderão apresentar as soluções criativas que foram utilizadas no
projeto, como o uso de ferramentas de visualização ou técnicas de pré-processamento
de dados. A criatividade é um aspecto importante em projetos de ciência de dados, pois
permite explorar novas abordagens e encontrar soluções inovadoras para problemas
complexos.
- Clareza e Coerência na Apresentação: Por fim, é importante que o projeto seja
apresentado de forma clara e coerente, tanto na apresentação oral como em qualquer
material escrito utilizado. Isso inclui a organização das informações em seções e
subseções, o uso adequado de gráficos e tabelas para ilustrar os resultados e a utilização
de uma linguagem clara e acessível.
o Nessa etapa HAVERÁ apresentação.
o Divisão de pontuação para avaliação do relatório disponível no Github do grupo:
  1. Apresentação do Projeto (máximo 3 pontos)
    - Qualidade do vídeo (1 ponto)
    - Clareza na exposição das ideias (1 ponto)
    - Criatividade na apresentação (1 ponto)
  2. Scripts no Github (máximo 2 pontos)
    - Clareza, documentação e organização do código (1 ponto)
    - Funcionalidade do código (1 ponto)
  3. Modelo de aprendizagem de máquina (máximo 2,5 pontos)
    - Seleção do modelo escolhido e justificativa para a escolha (1,5
  ponto)
    - Breve explicação sobre o funcionamento do modelo escolhido (1
  ponto)
  4. Balanceamento de dados, se necessário (máximo 0,5 ponto)
    - Explicação sobre a necessidade ou não de balanceamento de dados;e
    - Descrição do método utilizado para balanceamento, caso necessário
  5. Desenvolvimento do modelo (máximo 2 pontos)
    - Explicação detalhada dos passos realizados para o desenvolvimento
  do modelo (1 ponto)
    - Descrição das técnicas de pré-processamento utilizadas (1 ponto)
  6. Avaliação do modelo (máximo 2 pontos)
    - Apresentação das métricas utilizadas para avaliação do modelo (0,5
  ponto)
    - Descrição dos resultados obtidos e como interpretá-los (0,5 ponto)
    - Discussão sobre a validade das métricas utilizadas e sugestões de
  outras possíveis métricas (1 ponto)
  7. Conclusões (máximo 1 ponto)
    - Verificação se as conclusões obtidas estão coerentes com as
  perguntas levantadas na primeira etapa do projeto (0,5 ponto)
    - Discussão sobre possíveis limitações do modelo e sugestões para
  melhorias futuras (0,5 ponto)
  - Lembrando que todos os scripts gerados deverão estar disponibilizados até a data da
  entrega no Github e a apresentação do projeto deverá ser feita através de um vídeo que
  será disponibilizado no Youtube.
Obs.:
  1. O projeto deverá ser desenvolvido utilizando o GitHub como plataforma de armazenamento e
  controle de versão de todo o código e documentos gerados. É obrigatório que todos os scripts,
  documentos e afins estejam atualizados no GitHub até a data de entrega. Os documentos
  extraídos também deverão estar disponíveis no GitHub. O vídeo deverá ser postado no YouTube
  e o link deve ser disponibilizado no README.md do GitHub.
    a. Todos os documentos, scripts e códigos deverão ser disponibilizados no Github de
  forma organizada, o não atendimento dessa etapa levará a perda de 0,5 pontos;
    b. A organização do Github com README.MD e as pastas devidamente organizadas é
  primordial, não façam o upload de um projeto compactado. Aprendam a utilizar o
  Github da maneira correta. O não atendimento dessa etapa levará a perda de 0,5
  pontos;
    c. Além das entregas via Github, a entrega final será composta de um vídeo demonstrando
  o funcionamento do projeto. Esse vídeo deverá ser publicado no Youtube e o link
  deverá estar disponibilizado no README.MD do Github. O não atendimento dessa
  etapa levará a perda de 0,5 pontos;
  2. Para confirmar a entrega e receber a avaliação, será aberto um envio de trabalho no AVA. Nesse
  envio, deve-se compartilhar apenas o link do GitHub. É importante ressaltar que não serão
  aceitos trabalhos idênticos, total ou parcialmente, e também não serão aceitos cópias de trabalhos
  de terceiros.
  3. Este documento pode sofrer alterações ao longo do semestre, portanto, é importante que ele seja
  sempre consultado e mantido atualizado.
  4. A linguagem de programação utilizada é livre, ficando a critério do grupo escolher a mais
  adequada para a execução do projeto.
  5. Os encontros com o professor serão utilizados para tirar dúvidas, acompanhamento dos projetos
  e construção de objetivos. É importante que a cada encontro os participantes sejam objetivos
  com as dúvidas para que todos possam ser atendidos.
  6. Os participantes são responsáveis pelo próprio projeto, portanto, é importante serem organizados
  e traçarem objetivos alcançáveis para cada semana, a fim de facilitar a conclusão do projeto. Não
  deixem as etapas acumularem, caso tenham problemas, devem procurar o professor o quanto
  antes.