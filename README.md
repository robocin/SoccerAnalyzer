# Features as scripts

Essa branch possui algumas features que podem ser utilizadas como scripts individuais, para logs de 2D

## List of scripts:

### mean_stamina (multiple logs)

- Dado o caminho absoluto para diretório com um ou mútiplos arquivos de log, plota um gráfico de linha com a stamina média de cada time
  - Clique nas linhas dentro da caixa da legenda para esconder/mostrar cada uma das linhas correspondentes no gráfico.
- Uso: python3 mean_stamina.py <ABSOLUTE_PATH_TO_YOUR_DIRECTORY_HERE>

### fouls_position (single log)

- Dado o caminho absoluto para um arquivo .csv, plota o campo com as posições em que as faltas ocorreram.
- Uso: python3 fouls_position.py <ABSOLUTE_PATH_TO_YOUR_CSV_FILE_HERE>
