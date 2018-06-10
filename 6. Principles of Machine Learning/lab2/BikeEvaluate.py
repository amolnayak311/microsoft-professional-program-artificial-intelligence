
import pandas as pd

def ts_bikes(df, times):
    import matplotlib
    matplotlib.use('agg')
    import matplotlib.pyplot as plt
    for tm in times:        
        fig = plt.figure(figsize = (8, 6))
        fig.clf()
        ax = fig.gca()
        df_hr = df[df.hr == tm]
        df_hr.plot(kind = 'line', ax = ax, x = 'days', y = 'cnt', color = 'blue')
        df_hr.plot(kind = 'line', ax = ax, x = 'days', y = 'predicted', color = 'red')
        ax.set_xlabel('Days from start')
        ax.set_ylabel('Number of bikes rented')
        ax.set_title('Bikes rented for hour ' + str(tm))
        plt.savefig('ts_' + str(tm) + '.png')
    
 
def box_resids(df):
    import matplotlib
    matplotlib.use('agg')
    import matplotlib.pyplot as plt
    df['resids'] = df['predicted'] - df['cnt']    
    fig = plt.figure(figsize = (12, 6))
    ax = fig.gca()
    df.boxplot(column = 'resids', by = ['hr'], ax = ax)
    ax.set_xlabel('')
    ax.set_ylabel('Residuals')
    fig.savefig('resids.png')
    return df
 
def ts_resids_hist(df, times):
    import matplotlib
    matplotlib.use('agg')
    import matplotlib.pyplot as plt
    for time in times:
        df_time = df.ix[df.hr == time, ['resids']]
        fig = plt.figure(figsize = (8, 6))
        ax = fig.gca()
        df_time.hist(bins = 30, ax = ax)
        ax.set_xlabel('Residuals')
        ax.set_ylabel('Density')
        ax.set_title('Histogram of residuals by hour for hour ' + str(time))
        plt.savefig('hist_' + str(time) + '.png')
          
 
def azureml_main(df, dataframe2 = None):
    times = [6, 8, 10, 12, 14, 16, 18, 20, 22]
    df = df.sort(['days', 'hr'], axis = 0, ascending = True)
    ts_bikes(df, times)
    df = box_resids(df)
    ts_resids_hist(df, times)
    return df
