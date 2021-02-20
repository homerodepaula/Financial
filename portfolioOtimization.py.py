#otimização do portfolio (melhor alocação de pesos para cada ativo da carteira) (markowitz)
#importação basica +

import sys
def alocacao_portfolio(dataset, dinheiro_total, seed = 0, repeticoes):  	 #repeticoes quantos portfolios vao ser testados
	dataset = dataset.copy()
	dataset_original = dataset.copy()
	melhor_sharpe_ratio = 1 - sys.maxsize	
	melhores_pesos = np.empty


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

		dataset = dataset_original.copy()

	return melhor_sharpe_ratio, melhores_pesos

#testando
sharpe_ratio, melhores_pesos = alocacao_portfolio(pd.read_csv('usr/bin/finpython/data/acoesmulti.csv'), 5000, taxa_selic_historico.mean() / 100, 100)










