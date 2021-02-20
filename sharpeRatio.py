#sharpratio = calcula o retorno do investimento comparado com o risco
# S = (rp - rf)/σp     (rp = retorno esperado, rf = risk free)
#calcular retorno aculumado no periodo, desvio padrao e sharp ratio (um precisa do outro)
#importa o basico

dataset.loc[len(dataset) -1]['Valor Capital'] / dataset.loc[0]['Valor Capital'] - 1
dataset['Valor Capital'].std()

#calculo sharpRatio
(dataset['Valor Capital']).mean() / dataset['Valor Capital'].std() * np.sqrt(246) 	#sharp medio anual
