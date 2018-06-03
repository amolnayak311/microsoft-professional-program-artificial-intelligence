def id_outliers(df):
    df['outlier'] = [0] * df.shape[0]
    df.ix[df['enginesize'] > 190, 'outlier'] = 1
    df.ix[df['weight'] > 3500, 'outlier'] = 1
    df.ix[df['citympg'] > 40, 'outlier'] = 1
    return df


def auto_scatter_outliers(df, plot_cols):
    import matplotlib.pyplot as plt
    outlier = [0, 0, 1, 1]
    fuel = ['gas', 'diesel', 'gas', 'diesel']
    color = ['DarkBlue', 'DarkBlue', 'Red', 'Red']
    marker = ['x','o','o','x'] # vector of shape choices for plot 
    for col in plot_cols:
        fig = plt.figure(figsize = (6, 6))
        ax = fig.gca()
        for o, f, c, m in zip(outlier, fuel, color, marker):
            temp = df.ix[(df['outlier'] == o) & (df['fueltype'] == f), :]
            if temp.shape[0] > 0:
                temp.plot(kind = 'scatter', x = col, y = 'lnprice', marker = m, color = c, ax = ax)
            
        ax.set_title('Scatter plot of lnprice vs. ' + col)
        fig.savefig('scatter_' + col + '.png')
    
    #return plot_cols


def azureml_main(df):     
    import matplotlib
    matplotlib.use('agg')
    plot_cols = ["weight", "enginesize", "citympg"]
    df = id_outliers(df)
    auto_scatter_outliers(df, plot_cols)
    df = df[df.outlier == 1]
    return df 
