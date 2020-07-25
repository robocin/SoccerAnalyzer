from Position import Position

class PlotData:
    def __init__(self, graph_type, number_of_entries=0):
        # All types
        self.__name = None
        self.__entries = []
        self.__x_label = None
        self.__y_label = None


        # Specifc types 
        if(graph_type == "bar" or graph_type == "scatter" or graph_type == "pie"):
            for i in range(0, number_of_entries):
                self.__entries.append(Entry(graph_type))

        if(graph_type == "pie"):
            self.__sector_labels = None 
        

    # Setters and Getters
        # all
    def set_x_label(self, label):
        self.__x_label = label
    def set_y_label(self, label):
        self.__y_label = label
        # pie
    def set_sector_labels(self, labels):
        self.__sector_labels = labels
    
        # all
    def get_x_label(self):
        return self.__x_label
    def get_y_label(self):
        return self.__y_label
    def get_entries(self):
        return self.__entries
    def get_entry(self, entry_id):
        return self.__entries[entry_id]
        # pie
    def get_sector_labels(self):
        return self.__sector_labels

    # TODO: (discuss) Free instance
           #Python has in-built garbage collector it will delete the object as soon as reference count to the object becomes zero. 


class Entry:
    def __init__(self, entry_type):
        # All types
        self.__value = None
        self.__label = None

        # Specifc types
        if(entry_type == "bar"):
            self.__x_coordinate = None
            self.__height = None
            self.__width = 0.4
        if(entry_type == "pie"):
            self.__value = 0
        if(entry_type == "scatter"):
            self.__faults = []
            #TODO: PALIATIVO, APAGAR DEPOIS QUE TIVER SOLUÇÃO
            self.__x_positions = []
            self.__y_positions = []

	# Setters and Getters (all types)
    def set_value(self, value):
        self.__value = value
    def set_label(self, label):
        self.__label = label
	
    def get_value(self):
        return self.__value
    def get_label(self):
        return self.__label


	# Setters and Getters (specifc types)
        # bar
    def set_x_coordinate(self, x_coordinate):
        self.__x_coordinate = x_coordinate
    def set_height(self, height):
        self.__height = height
    def set_widht(self, width):
        self.__width = width

    def get_x_coordinate(self):
        return self.__x_coordinate
    def get_height(self):
        return self.__height
    def get_width(self):
        return self.__width

        # pie
    def set_value(self, value):
        self.__value = value
    def get_value(self):
        return self.__value
        
        # scatter
    def append_fault(self, fault):
        self.__faults.append(fault)
        #TODO: PALIATIVOS, APAGAR QUANDO TIVER SOLUÇÃO
    
    #TODO: DEPENDE DA SOLUÇÃO DE QUEM COMETEU A FALTA
    def _get_x_positions(self):
        x_positions = []
        for fault in self.__faults:
            x_positions.append(fault.get_position().get_x())
        return x_positions
    
    #TODO: DEPENDE DA SOLUÇÃO DE QUEM COMETEU A FALTA
    def _get_x_positions(self):
        y_positions = []
        for fault in self.__faults:
            y_positions.append(fault.get_position().get_y())
        return y_positions
    
    #TODO: FUNÇÕES PALIATIVAS(APAGAR QUANDO TIVER A SOLUÇÃO) 
    def set_x_positions(self, x_positions):
        self.__x_positions = x_positions
    def set_y_positions(self, y_positions):
        self.__y_positions = y_positions
    def get_x_positions(self):
        return self.__x_positions
    def get_y_positions(self):
        return self.__y_positions