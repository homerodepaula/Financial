import pandas as pd
import numpy as np
from pandas_datareader import data
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

#importando uma ação:
petro_df = data.DataReader(name = 'PETR4.SA', data_source = 'yahoo', start = '2015-01-01', end = '2015-12-31')

#infos:
petro_df.info()
petro_df.head(5) #5primeiros registros
petro_df.tail(5) #5ultimos registros
petro_df.describe() #mostra media, desvio padrao, minimo, 25%, 50%, 75%, maximo
petro_df[(petro_df['Close'] >= 16.90) && (petro_df['Close'] <= 21.40)]

#salvando:
petro_df.to_csv('petro.csv') #salvar pois pode ocorrer erro no yahoo finanças
#importando dnv:
petro_df2 = pd.read_csv('usr/bin/finpython/data/petro.csv')

#importando mais ações:
acoes = ['GOLL4.SA', 'CVCB3.SA', 'WEGE3.SA', 'MGLU3.SA', 'TOTS3.SA', 'BOVA11.SA']
acoes_df = pd.DataFrame()
for acao in acoes:
  acoes_df[acao] = data.DataReader(acao, data_source = 'yahoo', start = '2015-01-01', end = '2015-12-31)['Close']

#renomeando
acoes_df = acoes_df.rename(columns={'GOLL4.SA': 'GOL', 'CVCB3.SA': 'CVC', 'WEGE3.SA': 'WEG', 'MGLU3.SA': 'MAGALU', 'TOTS3.SA': 'TOTVS', 'BOVA11.SA': 'BOVESPA'})

#conferindo se tem valores nulos e eliminando:
acoes_df.isnull().sum()
acoes_df.dropna(inplace=True)

#salvando
acoes_df.to_csv('acoesmulti.csv')
