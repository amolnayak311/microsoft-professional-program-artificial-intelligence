 
import pandas as pd

def azureml_main(dataframe1 = None, dataframe2 = None):
    weekdays = [0, 1, 2, 3, 4, 5, 6]
    dayOfWeek = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    data = {'weekday': weekdays, 'dayOfWeek': dayOfWeek}
    return pd.DataFrame(data)

