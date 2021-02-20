#importa o de sempre
#multiplicar matriz risco pelo peso na carteira
pesos = np.array([0.5, 0.5])
np.dot(taxas_retorno_gol_cvc.cov() * 246, pesos)
np.dot(pesos, np.dot(taxas_retorno_gol_cvc.cov() * 246, pesos))                         #variancia
math.sqrt(np.dot(pesos, np.dot(taxas_retorno_gol_cvc.cov() * 246, pesos)))              #desvio padrao da carteira
pesos1 = np.array([0.2, 0.2, 0.2, 0.2, 0.2])                                            #novos pesos
pesos1.sum()
taxas_retorno
taxas_retorno.cov() * 240                                                               #buscando matriz de covariancia
np.dot(taxas_retorno.cov() *246 , pesos1)                                               
variancia_portfolio1 = np.dot(pesos1, np.dot(taxas_retorno.cov() *246 , pesos1))
volatilidade_portfolio1 = math.sqrt(variancia_portfolio1)
pesos2 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 1.0])                                       #pesos somente na bova (pode ser qualquer ETF)
variancia_portfolio2 = np.dot(pesos2, np.dot(taxas_retorno.cov() *246 , pesos2))
volatilidade_portfolio2 = math.sqrt(variancia_portfolio2)

#risco nao sistematico
#continuação do script

taxas_retorno.var() * 246   #anual
variancia_pesos1 = (taxas_retorno.var() *246) * pesos1
sub1 = variancia_pesos1[0] - variancia_pesos1[1] - variancia_pesos1[2] - variancia_pesos1[3] - variancia_pesos1[4] - variancia_pesos1[5]  
risco_nao_sistematico1 = (variancia_portfolio1 - sub1)
