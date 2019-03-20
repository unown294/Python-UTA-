class Employee:
	
	def __init__(self, id, name, depart, title):
		self.__name = name
		self.__depart = depart
		self.__title = title
		self.__id = id

	def set_name(self, name):
		self.__name = name
		
	def set_ID(self, id):
		self.__id = id

	def set_depart(self, depart):
		self.__depart = depart
	
	def set_title(self, title):
		self.__title = title
	
	# Accessors
	def get_ID(self):
		return self.__id
	def get_name(self):
		return self.__name
	def get_depart(self):
		return self.__depart
	def get_title(self):
		return self.__title
		
	def __str__(self):
		return "ID: " + str(self.__id) + \
			   "\nName: " + self.__name + \
		       "\ndepart: " + self.__depart + \
			   "\ntitle: " + self.__title
			   

	def __repr__(self):
		return "ID: " + str(self.__id) + \
                       "\nName: " + self.__name + \
                       "\ndepart: " + self.__depart + \
                       "\ntitle: " + self.__title
			   
