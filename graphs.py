#importing ; lib importada no import.

#histograma (distribuição de frequencia)
acoes_df = pd.read_csv('usr/bin/finpython/data/acoesmulti.csv')
sns.histplot(acoes_df['GOL'], bins=10);  #bins quantidade de colunas
plot.figure(figsize=(10,50))
i=1
for i in np.arrange(1, len(acoes_df.columns)):
  plt.subplot(7, 1, i+1)
  sns.histplot(acoes_df[acoes_df.columns[i]] kde = True) #kde linha de densidade
  plt.title(acoes_df.columns[i])

#boxplot
sns.boxplot(x = acoes_df['GOL]);
i=1
for i in np.arrange(1, len(acoes_df.columns)):
  plt.subplot(7, 1, i+1)
  sns.boxplot(acoes_df[acoes_df.columns[i]])
  plt.title(acoes_df.columns[i])

#linhas
acoes_df.plot(x = 'Date', figsize = (15,7), title = 'Historico do preço');

#normalização
acoes_df_normalizado = acoes_df.copy()
for i in acoes_df_normalizado.columns[1:]:
  acoes_df_normalizado[i] = acoes_df_normalizado[i] / acoes_df_normalizado[i][0]

#conferindo
acoes_df_normalizado.plot(x = 'Date', figsize = (15,7), title = 'Historico do preço - NORMALIZADO');

#Grafico Dinamico
figura = px.line(title = 'Histórico do preço das ações')
for i in acoes_df_columns[1:]:
  figura.add_scatter(x = acoes_df['Date'], y = acoes_df[i], name = i)
figura.show()
