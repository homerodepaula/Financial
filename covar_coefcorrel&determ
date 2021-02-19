#importa o de sempre
#teoria:
#covariancia = C(x,y) = £[(xi - X) * (yi - Y)]/n-1                   #>0 msm lado, <0 direcoes opostas, 0 var independentes
#coeficiente de correlação = CR(x,y) = Cov(x,y) / std(x) * std (y)
#coeficiente de determinação = CD(x,y) = Cr²                         #quantos % da variavel dependente consegue ser explicada pela var explanatoria

taxas_retorno.cov()
taxas_retorno.corr()
taxas_retorno.corr() ** 2

#covariancia e correlaçao entre empresas
taxas_retorno_gol_cvc = taxas_retorno.drop(columns = ['WEGE', 'MAGALU', 'BOVESPA', 'TOTVS'])
taxas_retorno_gol_cvc.cov()
#gerando matriz de covariancia
taxas_retorno_gol_cvc.cov() * 246
