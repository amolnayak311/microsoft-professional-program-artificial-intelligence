import pandas as pd

def azureml_main(df):
    df['admission_type_description'] = ['unknown' if x in ['Not Available', 'Not Mapped', 'NULL'] else x for x in df['admission_type_description']]
    return df
