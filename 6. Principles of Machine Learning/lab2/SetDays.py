import pandas as pd


def azureml_main(df, dataframe2 = None):    
    df['days'] = pd.Series(data = range(df.shape[0])) // 24
    return df
