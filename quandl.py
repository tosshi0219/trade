import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np
import pandas as pd
from pandas import Series,DataFrame
import quandl
quandl.ApiConfig.api_key = 'Z558rxTFcPPFPyAU44UH'

df_nikkei = quandl.get("NIKKEI/ALL_STOCK")   #日経平均
df_jasdaq=quandl.get("NIKKEI/JASDAQ")    #JASDAQ
df_jpus=quandl.get("FRED/DEXJPUS")      #日米為替
df_interest_10y=quandl.get("MOFJ/INTEREST_RATE_JAPAN_10Y")   #10年国債利回り
df_oil_index=quandl.get("TOCOM/INDEX_O")    #原油価格
df_gold_index=quandl.get("TOCOM/INDEX_GC")   #金価格
df_silver_index=quandl.get("TOCOM/INDEX_SI")   #銀価格
df_copper_index=quandl.get("COM/COPPER")    #銅価格

df1_nikkei= df_nikkei.rename(columns={'Close': 'NIKKEI'})
df1_jasdaq=df_jasdaq.drop(['Open', 'High','Low'], axis=1)
df2_jasdaq = df_jasdaq1.rename(columns={'Close': 'JASDAQ'})
df1_jpus= df_jpus.rename(columns={'Value': '日米為替'})
df1_interest_10y= df_interest_10y.rename(columns={'Value': '10年国債利回り'})
df1_oil_index= df_oil_index.rename(columns={'Index': 'OIL'})
df1_gold_index= df_gold_index.rename(columns={'Index': 'GOLD'})
df1_silver_index= df_silver_index.rename(columns={'Index': 'SILVER'})
df1_copper_index= df_copper_index.rename(columns={'Value': 'COPPER'})

df=pd.concat([df1_nikkei,
                          df2_jasdaq,
                          df1_jpus,
                          df1_interest_10y,
                          df1_oil_index,
                          df1_gold_index,
                          df1_silver_index,
                          df1_copper_index],axis=1)

df_data=df.dropna()
print(df_data)

#描画する
plt.figure(figsize=(20,20))
#plt.plot(df1_nikkei)
#plt.plot(df2_jasdaq)
#plt.plot(df1_jpus)
#plt.plot(df1_interest_10y)
#plt.plot(df1_oil_index)
#plt.plot(df1_gold_index)
#plt.plot(df1_silver_index)
#plt.plot(df1_copper_index)
plt.show()
plt.close('all')
