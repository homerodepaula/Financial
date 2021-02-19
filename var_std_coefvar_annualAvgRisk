#teoria: Media: X = £Xi / n         
#teoria: Variancia: σ² = £(x1- X)² / N
#teoria: Desvio padrão: σ 
#importa o basico pra variar

dataset = pd.read_csv('usr/bin/finpython/data/acoesmulti.csv')
taxas_cvc = np.array([-11.8, 63.73, 74.52, 20.42, -33,29, -128,06])                 #taxas de retorno anuais

#calculo media
media_cvc = taxas_cvc.sum() / len(taxas_cvc)
#ou
media_cvc = taxas_cvc.mean()

#variancia
(taxas_cvc - media_cvc) ** 2.sum() / len(taxas_cvc)
#ou
variancia_cvc = taxas_cvc.var()

#desvio padrao (raiz quadrada da variancia)
desvio_padrao_cvc = math.sqrt(variancia_cvc)

#coeficiente de variacao
#teoria: CV = σ/X *100
coeficiente_variacao_cvc = (desvio_padrao_cvc / media_cvc) * 100
#ou
stats.variation(taxas_cvc) * 100

#Risco medio anual
dataset = pd.read_csv('usr/bin/finpython/data/acoesmulti.csv')
dataset.drop(labels = ['Date'], axis = 1, inplace = True)
taxas_retorno = (dataset / dataset.shift(1)) -1
taxas_retorno.std() * math.sqrt(246)                          #anualizando
