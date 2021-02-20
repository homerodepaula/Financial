#otimização do portfolio (melhor alocação de pesos para cada ativo da carteira) (markowitz)
#importação basica +

import sys
def alocacao_portfolio(dataset, dinheiro_total, sem_risco, repeticoes):  	 #repeticoes quantos portfolios vao ser testados
	dataset = dataset.copy()
	dataset_original = dataset.copy()
	
	lista_retorno_esperado = []
	lista_volatilidade_esperada = []					#usado na visualizaçao grafica
	lista_sharpe_ratio = []
	
	melhor_sharpe_ratio = 1 - sys.maxsize	
	melhores_pesos = np.empty
	melhor_volatilidade = 0
	melhore_retorno = 0

	for _ in range(repeticoes):						#executa a quantidade de vezes de repeticoes
		pesos = np.random.random(len(dataset.columns) -1)
		pesos = pesos / pesos.sum()			
	
		for i in dataset.columns[1:]:
			dataset[i] = dataset[i] / dataset[i][0]

		for i, acao in enumerate(dataset.columns[1:]):
			dataset[acao] = dataset[acao] * pesos[i] * dinheiro_total
	
		dataset.drop(labels = ['Date'], axis = 1, inplace = True)	
		
		retorno_carteira = np.log(dataset / dataset.shift(1))
		matriz_covariancia = retorno_carteira.cov()

		dataset['Valor Capital'] = dataset.sum(axis = 1)
		dataset['taxa de retorno'] = 0.0

		for i in range(1, len(dataset)):				#taxa de retorno logaritmica(msm acao)
			dataset['taxa de retorno'][i] = np.log(dataset['Valor Capital'][i] / dataset['Valor Capital'] [i - 1])
	
		#sharpe_ratio = (dataset['taxa de retorno'].mean() - sem_risco) / dataset['taxa de retorno].std() * np.sqrt(246)
		retorno_esperado = np.sum(dataset['taxa de retorno'].mean * pesos) * 246	#retorno medio anual c peso		
		volatilidade_esperada = np.sqrt(np.dot(pesos, np.dot(matriz_covariancia * 246, pesos)))	
		sharpe_ratio = (retorno_esperado - sem_risco) / volatilidade_esperada
	
		if sharpe_ratio > melhor_sharpe_ratio:
			melhor_sharpe_ratio = sharpe_ratio
			melhores_pesos = pesos
			melhor_volatilidade = volatilidade_esperada
			melhor_retorno = retorno_esperado
		lista_retorn_esperado.append(retorno_esperado)
		lista_volatilidade_esperada.append(volatilidade_esperada)
		lista_sharpe_ratio.append(sharpe_ratio)
		
		dataset = dataset_original.copy()

	return melhor_sharpe_ratio, melhores_pesos, lista_retorno_esperado, lista_volatilidade_esperada, lista_sharpe_ratio, melhor_volatilidade, melhor_retorno

#testando
sharpe_ratio, melhores_pesos = alocacao_portfolio(pd.read_csv('usr/bin/finpython/data/acoesmulti.csv'), 5000, taxa_selic_historico.mean() / 100, 100)
