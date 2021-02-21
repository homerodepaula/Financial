#portfolioVisualization
#imports basicos

figura = px.line(x = datas, y = dataset['Valor Capital'], title = 'Retorno diário do portfolio')
figura = px.line(title = 'Evolução do patrimonio')
for i in dataset.drop(columns = ['Valor Capital', 'taxa de retorno']).columns:
	figura.add_scatter(x = datas, y = dataset[i], name = i)				#cada uma das acoes
figura = px.line(x = datas, y = dataset['Valor Capital'], title = 'Evolução do patrimonio')

#é só pra visualizar acao com % que foi alocado para cada ativo

def visualiza_alocacao(solucao):						#visualiza a solução do problema (portAloc)
	colunas = dataset_original.columns[1:]
	for i in range(len(solucao)):
		print(colunas[i], solucao[i] *100)				#pspsps
