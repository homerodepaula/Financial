#taxa de retorno simples, taxa de retorno logaritmico, analise de carteiras
#teoria do calculo (t.r. simples): rs = (precoFinal - precoInicial) / precoInicial  *100(se quiser em percentual)
#Dividendos entra no preço final(soma), tx de compra e venda entra no preço inicial
#lucro seria = precoVenda + dividendos - precoCompra - tx compra - tx venda

#importa-se as bibliotecas no main e vem.
dataset = pd.read_csv('usr/bin/finpython/data/acoesmulti.csv')

#taxa de retorno simples:
dataset ['GOL'][0], dataset['GOL'][len(dataset) - 1]

((dataset['GOL'][len(dataset) -1] - dataset['GOL'][0]) / dataset['GOL'][0]) * 100
((dataset['WEGE'][len(dataset) -1] - dataset['WEGE'][0]) / dataset['WEGE'][0]) * 100
((dataset['CVC'][len(dataset) -1] - dataset['CVC'][0]) / dataset['CVC'][0]) * 100
((dataset['TOTVS'][len(dataset) -1] - dataset['TOTVS'][0]) / dataset['TOTVS'][0]) * 100
((dataset['BOVESPA'][len(dataset) -1] - dataset['BOVESPA'][0]) / dataset['BOVESPA'][0]) * 100
((dataset['MAGALU'][len(dataset) -1] - dataset['MAGALU'][0]) / dataset['MAGALU'][0]) * 100
#OU (dataset['MAGALU'][len(dataset) -1] / dataset['MAGALU'][0] -1) * 100                #DA NO MESMO

#taxa de retorno diária 
dataset['GOL'].shift(1)   #abre espaço no primeiro registro (tamanho 1)

dataset['RS GOL'] = (dataset['GOL'] / dataset['GOL'].shift(1)) - 1
dataset['RS WEGE'] = (dataset['WEGE'] / dataset['WEGE'].shift(1)) - 1
dataset['RS CVC'] = (dataset['CVC'] / dataset['CVC'].shift(1)) - 1
dataset['RS TOTVS'] = (dataset['TOTVS'] / dataset['TOTVS'].shift(1)) - 1
dataset['RS BOVESPA'] = (dataset['BOVESPA'] / dataset['BOVESPA'].shift(1)) - 1
dataset['RS MAGALU'] = (dataset['MAGALU'] / dataset['MAGALU'].shift(1)) - 1

#taxa media de retorno diaria
dataset['RS GOL'].mean()

#taxa de retorno anual
(dataset['RS GOL'].mean() * 246) * 100     #se quiser em % e funciona 246 dias no ano a bolsa
(dataset['RS WEGE'].mean() * 246) * 100
(dataset['RS CVC'].mean() * 246) * 100
(dataset['RS TOTVS'].mean() * 246) * 100
(dataset['RS BOVESPA'].mean() * 246) * 100
(dataset['RS MAGALU'].mean() * 246) * 100

#taxa de retorno logaritmica (msm acao em periodos diferentes)
#teoria: rl = log(precoFinal - precoInicial)/precoInicial *100
#lucro = precoFinal + dividendos - precoInicial - tx compra - tx venda

np.log(dataset['GOL'][len(dataset) -1] /dataset['GOL'][0]) *100
np.log(dataset['WEGE'][len(dataset) -1] /dataset['WEGE'][0]) *100
np.log(dataset['CVC'][len(dataset) -1] /dataset['CVC'][0]) *100
np.log(dataset['TOTVS'][len(dataset) -1] /dataset['TOTVS'][0]) *100
np.log(dataset['BOVESPA'][len(dataset) -1] /dataset['BOVESPA'][0]) *100
np.log(dataset['MAGALU'][len(dataset) -1] /dataset['MAGALU'][0]) *100

#tx de retorno logaritmica diaria

dataset['RL GOL'] = np.log(dataset['GOL'] / dataset['GOL'].shift(1))
dataset['RL WEGE'] = np.log(dataset['WEGE'] / dataset['WEGE'].shift(1))
dataset['RL CVC'] = np.log(dataset['CVC'] / dataset['CVC'].shift(1))
dataset['RL TOTVS'] = np.log(dataset['TOTVS'] / dataset['TOTVS'].shift(1))
dataset['RL BOVESPA'] = np.log(dataset['BOVESPA'] / dataset['BOVESPA'].shift(1))
dataset['RL MAGALU'] = np.log(dataset['MAGALU'] / dataset['MAGALU'].shift(1))

#tx de retorno logaritmica anual
(dataset['RL GOL'].mean() * 246) * 100
(dataset['RL WEGE'].mean() * 246) * 100
(dataset['RL CVC'].mean() * 246) * 100
(dataset['RL TOTVS'].mean() * 246) * 100
(dataset['RL BOVESPA'].mean() * 246) * 100
(dataset['RL MAGALU'].mean() * 246) * 100
