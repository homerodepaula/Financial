#portfolioVisualization
#imports basicos

figura = px.line(x = datas, y = dataset['Valor Capital'], title = 'Retorno diário do portfolio')
figura = px.line(title = 'Evolução do patrimonio')
for i in dataset.drop(columns = ['Valor Capital', 'taxa de retorno']).columns:
	figura.add_scatter(x = datas, y = dataset[i], name = i)				#cada uma das acoes
figura = px.line(x = datas, y = dataset['Valor Capital'], title = 'Evolução do patrimonio')