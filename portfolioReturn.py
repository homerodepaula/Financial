#retorno carteira de acoes
#importa as library como de costume la atrás

dataset = pd.read_csv('usr/bin/finpython/data/acoesmulti.csv')

#normalizando
dataset_normalizado = dataset.copy()
for i in dataset_normalizado.columns[1:]:
  dataset_normalizado[i] = (dataset_normalizado[i] / dataset_normalizado[i][0])
dataset_normalizado.drop(labels = ['Date'], axis = 1, inplace = True)
#retornos
retorno_carteira = (dataset_normalizado / dataset_normalizado.shift(1)) -1  #retorno simples pois é no mesmo periodo de tempo de varias açoes.
retorno_anual = retorno_carteira.mean() * 246                               #retorno logaritmico é msm ação em diferentes periodos de tempo.
retorno_atual = retorno_atual * 100                                         #para mostrar em %

#tx de retorno de uma carteira (desconsiderando bovespa p/ calculo como indice Beta)
#deve-se definir o peso de cada ativo na carteira (total = 1,0) ou pode ser peso igual
pesos_carteira1 = np.array([0.2,0.2,0.2,0.2,0.2,0.0]                        #0.0 para zerar o valor do bovespa
pesos_carteira1.sum()                                                       #deve ser igual a um
np.dot(retorno_anual, pesos_carteira1)                                      #calculo do retorno medio anual (sem bova) carteira1
pesos_carteira2 = np.array([0.1,0.2,0.3,0.1,0.3,0.0]
pesos_carteira2.sum()
np.dot(retorno_anual, pesos_carteira2)                                      #calculo do retorno medio anual (sem bova) carteira2

#comparativo carteira com bovespa (Benchmark)
dataset = pd.read_csv('usr/bin/finpython/data/acoesmulti.csv')
dataset_normalizado = dataset.copy()
for i in dataset_normalizado.columns[1:]:
  dataset_normalizado[i] = (dataset_normalizado[i] / dataset_normalizado[i][0])
dataset_normalizado['CARTEIRA'] = (dataset_normalizado['GOL'] + dataset_normalizado['WEGE'] + 
                                   dataset_normalizado['CVC'] + dataset_normalizado['TOTVS'] + 
                                   dataset_normalizado['MAGALU']) / 5
figura = px.line(title = 'Comparativo carteira x Bova')
for i in dataset_normalizado.columns[1:]:
  figura.add_scatter(x = dataset_normalizado['Date'], y = dataset_normalizado[i], name = 1)

#para comparar apenas carteira x Bovespa
dataset_normalizado.drop(['GOL', 'WEGE', 'CVC', 'MGLU', 'TOTS'], axis = 1, inplace = True)

figura = px.line(title = 'Comparativo carteira x Bova')
for i in dataset_normalizado.columns[1:]:
  figura.add_scatter(x = dataset_normalizado['Date'], y = dataset_normalizado[i], name = 1)
