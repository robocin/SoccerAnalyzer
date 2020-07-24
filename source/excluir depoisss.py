em mainwindow 205:

			# COMENTADO A SEGUIR, TEST PIE e TEST BAR deverão ser excluídos, inclusive da lista, estão aqui apenas para servir de referência durante o desenvolvimento.

"""
		elif(graph_type == "TEST PIE"):
			self.plot_Pie("TEST PIE - APENAS PARA REFERÊNCIA ")
		elif(graph_type == "TEST BAR"):
			
			data = PlotData() # COMENTÁRIOS (Felipe)
							  # não está sendo inicializado, falta parâmetros
							  # Opção: 1
							  #	 Parametrizar
							  # Opção: 2
							  #	 Inicializar com parâmetros default na própria classe 
			
			data.appendBars(1,["test bar"]) # Este método não está definido no PlotData
			
			data.set_x_label("x label")
			data.set_y_label("y label")
			
			bar = data.getBar(0) # ESta método não está definida no PlotData
			
			bar.set_name("Bar name")
			bar.set_value(100) 
			bar.set_label("Bar label")
			
			self.plot_Bar("TEST BAR - APENAS PARA REFERÊNCIA",data)
		'''(...)'''
"""

def plot_Pie(self, title):

        data = [50,50]
        label = ["A","B"]

        # create an axis
        ax = self.figure.add_subplot(111)

        # plot data
        ax.pie(data, labels = label)

        # set title
        ax.set_title(title)

        #TODO: is this necessary?
        # discards the old graph
        #ax.clear()
 
        #TODO: is this necessary?
        # refresh canvas
        #self.canvas.draw()