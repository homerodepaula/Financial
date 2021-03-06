#stockPicker
#definição de pesos para as ações, sharpe ratio, calculo de markowitz
#alocação randomica de pesos, algoritmos de otimização
#alocação e otimização de portfolios

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

dataset = pd.read_csv('usr/bin/finpython/data/acoesmulti.csv')

def alocacao_ativos(dataset, dinheiro_total, seed = 0, melhores_pesos = []):
  	dataset = dataset.copy()
	if seed != 0:
		np.random.seed(seed)
	if len(melhores_pesos) > 0:
		pesos = melhores_pesos
	else:
		pesos = np.random.random(len(dataset.columns) - 1)
		pesos = pesos / pesos.sum()				#normalizando
	
#normalizando ds e dropando data
	colunas = dataset.columns[1:] 
	for i in colunas:
		dataset[i] = (dataset[i] / dataset[i][0])	

	for i, acao in enumerate(dataset.columns[1:]):
		dataset[acao] = dataset[acao] * pesos[i] * dinheiro_total

	dataset['Valor Capital'] = dataset.sum(axis = 1)
	datas = dataset['Datas']
	dataset.drop(labels = ['Date'], axis = 1, inplace = True)
	dataset['taxa de retorno'] = 0.0
	for i in range(1, len(dataset)): 				#populando
		dataset['taxa retorno'][i] = ((dataset['Valor Capital'][i] / dataset['Valor Capital'][i - 1]) - 1) * 100
	
	acoes_pesos = pd.DataFrame(data = {'Ações': colunas, 'Pesos: pesos *100})
	
	return dataset, datas, acoes_pesos, dataset.loc[len(dataset) - 1]['Valor Capital']  #ultima linha(len-1) e ultima coluna(nomeada)

dataset, datas, acoes_pesos, soma_valor = alocacao_ativos(pd.read_csv('usr/bin/finpython/data/acoesmulti.csv'), 5000, 10)
