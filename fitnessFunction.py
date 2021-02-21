#hill climb, simulated annealing, algoritmo genético:
#biblioteca mlrose (algoritmo usado quando precisa maximizar ou minimizar valores, neste caso sharpe ratio)
#tem q instalar o mlrose pelo pip (1.3.0)

import mlrose

dataset_original = pd.read_csv('usr/bin/finpython/data/acoesmulti.csv')
dinheiro_total = 5000
sem_risco = taxa_selic_historico.mean() / 100

def fitness_function(solucao):
	dataset = dataset_original.copy()
	pesos = solucao / solucao.sum()	 								#normalização pro somatorio de pesos ser igual a 1
	for i in dataset.columns[1:]:
		dataset[i] = dataset[i] / dataset[i][0]

	for i, acao in enumerate(dataset.columns[1:]):
		dataset[acao] = dataset[acao] * pesos[i] * dinheiro_total
	dataset.drop(labels = ['Date'], axis = 1, inplace = True)
	dataset['Valor Capital'] = dataset.sum(axis = 1)
	for i in range(1, len(dataset)):
		dataset['taxa de retorno'][i] = ((dataset['Valor Capital'][i] / dataset['Valor Capital'] [i-1]) - 1) * 100
	sharpe_ratio = (dataset['taxa de retorno'].mean()- sem_risco) / dataset['taxa de retorno'].std() * np.sqrt(246)
	
	return sharpe_ratio

np.random.seed(10)
pesos = np.random.random(len(dataset_original.columns) - 1)
pesos = pesos / pesos.sum()	
