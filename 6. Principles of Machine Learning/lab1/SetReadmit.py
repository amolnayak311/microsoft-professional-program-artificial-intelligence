import pandas as pd

def azureml_main(df):
    df.ix[df['readmitted'] != 'NO', 'readmitted'] = 'YES'    
    return df