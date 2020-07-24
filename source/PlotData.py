class PlotData:
    def __init__(self, graph_type, number_of_entries):
        # All types
        self.__name = None
        self.__entries = []
        self.__x_label = None
        self.__y_label = None


        # Specifc types 
        if(graph_type == "bar"):
            for i in range(0, number_of_entries):
                self.__entries.append(Entry("bar"))
        
        if(graph_type == "pir"):
            pass
        
        if(graph_type == "scatter"):
            pass

    # Setters and Getters
    def set_x_label(self, label):
        self.__x_label = label
    def set_y_label(self, label):
        self.__y_label = label
    
    def get_x_label(self):
        return self.__x_label
    def get_y_label(self):
        return self.__y_label
    def get_entries(self):
        return self.__entries

    def get_entry(self, entry_id):
        return self.__entries[entry_id]

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
            self.__width = None

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
        #bar
    def set_x_coordinate(self, x_coordinate):
        self.__x_coordinate = x_coordinate
    def set_height(self, height):
        self.__height = height

    def get_x_coordinate(self):
        return self.__x_coordinate
    def get_height(self):
        return self.__height


