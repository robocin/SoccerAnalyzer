from Position import Position

class PlotData:
    def __init__(self, graph_type=None, title="ZMissing Title", number_of_entries=0):
        # All types
        self.__title = title
        self.__entries = []
        self.__x_label = None
        self.__y_label = None
        self.__background_image = None
        self.__show_background_image = False

        # Instance the entries
        for i in range(0, number_of_entries):
                self.__entries.append(Entry(graph_type))
        

    # Setters and Getters
        # all
    def set_x_label(self, label):
        self.__x_label = label
    def set_y_label(self, label):
        self.__y_label = label
    def set_background_image(self, img):
        self.__background_image = img

    def get_x_label(self):
        return self.__x_label
    def get_y_label(self):
        return self.__y_label
    def get_entries(self):
        return self.__entries
    def get_entry(self, entry_id):
        return self.__entries[entry_id]
    def get_background_image(self):
        return self.__background_image

    def show_background_image(self):
        self.__show_background_image = True
    def hide_background_image(self):
        self.__show_background_image = False
    def is_background_image_visible(self):
        return self.__show_background_image


class Entry:
    def __init__(self, graph_type):
        # All types
        self.__value = None
        self.__values = []
        self.__label = None
        self.__x_label = "X"
        self.__y_label = "Y"
        self.__x_coordinate = None
        self.__y_coordinate = None
        self.__color = "grey"

        # Bar
        if (graph_type == "bar"):
            self.__width = 0.4

	# Setters and Getters (all types)
    def set_value(self, value):
        self.__value = value
    def set_values(self, value):
        self.__value = value
    def set_label(self, label):
        self.__label = label
    def set_x_label(self, label):
        self.__x_label = label
    def set_y_label(self, label):
        self.__y_label = label
    def set_x_coordinate(self, value):
        self.__x_coordinate = value
    def set_y_coordinate(self, value):
        self.__y_coordinate = value
    def set_color(self, color):
        self.__color = color
	
    def get_value(self):
        return self.__value
    def get_values(self):
        return self.__value
    def get_label(self):
        return self.__label
    def get_x_label(self):
        return self.__x_label
    def get_y_label(self):
        return self.__y_label
    def get_x_coordinate(self):
        return self.__x_coordinate
    def get_y_coordinate(self):
        return self.__y_coordinate
    def get_color(self):
        return self.__color
    
    # Bar
    def set_widht(self, width):
        self.__width = width

    def get_width(self):
        return self.__width