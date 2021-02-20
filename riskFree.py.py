#calculo para tpf selic

dinheiro_total = 5000						#ex

taxa_selic_2015 = 12.75
taxa_selic_2016 = 14.25
taxa_selic_2017 = 12.25
taxa_selic_2018 = 6.50
taxa_selic_2019 = 5.0
taxa_selic_2020 = 2.0

valor_2015 = dinheiro_total + (dinheiro_total * taxa_selic_2015 / 100)
valor_2016 = valor_2015 + (valor_2015 * taxa_selic_2016 / 100)
valor_2017 = valor_2016 + (valor_2016 * taxa_selic_2017 / 100)
valor_2018 = valor_2017 + (valor_2017 * taxa_selic_2018 / 100)
valor_2019 = valor_2018 + (valor_2018 * taxa_selic_2019 / 100)
valor_2020 = valor_2019 + (valor_2019 * taxa_selic_2020 / 100)

rendimentos = valor_2020 - dinheiro_total			#mostra quanto dinheiro ganhou 

#Imposto de renda
ir = rendimentos * 15/100

valor_2020 - ir

#sharp ratio
taxa_selic_historico = np.array([12.75, 14.25, 12.25, 6.5, 5.0, 2.0])
(dataset['taxa de retorno'].mean() - taxa_selic_historico.mean() / 100) / dataset['taxa de retorno'].std() * np.sqrt(246)