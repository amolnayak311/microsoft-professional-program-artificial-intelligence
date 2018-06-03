
def auto_scatter_simple(df, plot_cols):
	import matplotlib.pyplot as plt
	for col in plot_cols:
		fig = plt.figure(figsize = (6, 6))
		ax = fig.gca()
		df.plot(kind = 'scatter', ax = ax, x = col, y = 'lnprice', color = 'DarkBlue')
		ax.set_title('Scatter plot of price vs. ' + col)
		fig.savefig('scatter_' + col + '.png')
	
    #return plot_cols
	
def azureml_main(df):     
	import matplotlib     
	matplotlib.use('agg')    
	## Define plot columns     
	plot_cols = ["weight", "enginesize", "citympg"]     
	auto_scatter_simple(df, plot_cols) 
	## Create plots
	return df 
	
	
	
