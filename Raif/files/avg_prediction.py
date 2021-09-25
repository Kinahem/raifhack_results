import pandas as pd

df1 = pd.read_csv('catb_ot_no_mult_stkfold_10cl.csv', index_col='id')
df2 = pd.read_csv('submission0.1266_catb.csv', index_col='id')
df3 = pd.read_csv('submit_full_featurs_with_external_data_lgbm.csv', index_col='id')

final_df = (df1+df2/0.9+df3)/3

final_df.to_csv('final_sub.csv')
